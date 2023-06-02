import requests
import matplotlib.pyplot as plt
import dateutil.parser

class Weather:
    def __init__(self, street, city, state, zipcode, loc_name, hour):
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.loc_name = loc_name
        # print(self.zipcode)
        if hour == 'd':
            self.getForecastdaily()
            self.getTempsdaily()
        elif hour == 'h':
            self.getForecasthourly()
            self.getTempsHourly()
    
    def getForecasthourly(self):
        geocode = requests.get("https://geocoding.geo.census.gov/geocoder/locations/address?street={}&city={}&state={}&zip={}&benchmark=4&format=json".format(self.street, self.city, self.state, self.zipcode))
        #print(geocode.text)
        coordinates = geocode.json()['result']['addressMatches'][0]['coordinates']
        gridpoints = requests.get('https://api.weather.gov/points/{},{}'.format(coordinates['y'],coordinates['x']))
        #print(gridpoints.text)
        self.forecast = requests.get(gridpoints.json()['properties']['forecastHourly'])
        # print(self.forecast.text) # uncomment to print raw forecast info
    def getTempsHourly(self):
        #print(self.forecast.text)
        time = str(self.forecast.json()['properties']['periods'][0]['startTime'])
        time = time[-5:]
        hour = int(time[:-3])
        tick = 0
        self.times, self.temp = [], []
        for hr in self.forecast.json()['properties']['periods']:
            time = str(hour) + ':00'
            self.times.append(time)
            self.temp.append(hr['temperature'])
            hour += 1
            if hour == 25:
                hour = 1
            tick += 1
            if tick == 24:
                break
    def getForecastdaily(self):
        geocode = requests.get("https://geocoding.geo.census.gov/geocoder/locations/address?street={}&city={}&state={}&zip={}&benchmark=4&format=json".format(self.street, self.city, self.state, self.zipcode))
        #print(geocode.text)
        coordinates = geocode.json()['result']['addressMatches'][0]['coordinates']
        gridpoints = requests.get('https://api.weather.gov/points/{},{}'.format(coordinates['y'],coordinates['x']))
        self.forecast = requests.get(gridpoints.json()['properties']['forecast'])
        # print(self.forecast.text) # uncomment to print raw forecast info
    def getTempsdaily(self):
        self.timesDay, self.tempsDay, self.timesNight, self.tempsNight = [], [], [], []
        for days in self.forecast.json()['properties']['periods']:
            if days['isDaytime']:
                self.timesDay.append(dateutil.parser.parse(days['startTime']))
                self.tempsDay.append(days['temperature'])
            else:
                self.timesNight.append(dateutil.parser.parse(days['startTime']))
                self.tempsNight.append(days['temperature'])
    def txt_display_forecast(self):
        for days in self.forecast.json()['properties']['periods']:
            print('{}:\n{}{}, {}\n\n'.format(days['name'], days['temperature'], days['temperatureUnit'], days['shortForecast']))
def plt_display_forecast(item, hour):
    if hour == 'd':
        for lis in item:
            plt.plot(lis.timesDay, lis.tempsDay, 'o-', label=lis.loc_name + ' day')
            plt.plot(lis.timesNight, lis.tempsNight,'o-', label=lis.loc_name + ' night')
        plt.title('temp for next seven days')
    else:
        for lis in item:
            plt.plot(lis.times, lis.temp, 'o-', label=lis.loc_name)
        plt.title('temp for 24 hours')
    plt.gcf().autofmt_xdate()
    plt.xlabel('days')
    plt.ylabel('temp (in F)')
    plt.grid()
    plt.legend()
    plt.show()

# get the weather of the white house
ny_near_street = '1+Scott+Ave'
ny_near_city = 'Yougstown'
ny_near_state = 'NY'
ny_near_zipcode = "14174"

ny_street = '20+W+34th+st'
ny_city = 'New York'
ny_state = 'NY'
ny_zipcode = '10001'

dc_street = "1600+Pennsylvania+Avenue+NW"
dc_city = "Washington"
dc_state = "DC"
dc_zipcode = "20500"
other_street = (input('What is the number of your loc   ') + '+' + input('What is the road name   ') + '+' + input('What is the dr, ave, rd, etc   '))
other_city = input('What is the city name?   ')
i = 0
for ob in other_city:
    if ob == ' ':
        other_city = other_city[:i] + '+' + other_city[i+1:]
    i += 1
other_state = input('What is the name of the state   ')
while True:
    try:
        other_zipcode = int(input('What is the zipcode  '))
        break
    except:
        print('That is not a number')
other_name = input('What is the name of this place?   ')

hour = input('Would you like hourly or daily?  (h/d)  ')

NY_near = Weather(ny_near_street, ny_near_city, ny_near_state, ny_near_zipcode, 'NY Near', hour)
DC = Weather(dc_street, dc_city, dc_state, dc_zipcode, 'DC', hour)
NY = Weather(ny_street, ny_city, ny_state, ny_zipcode, 'NY', hour)
try:
    other = Weather(other_street, other_city, other_state, other_zipcode, other_name, hour)
    locs = [NY, DC, NY_near, other]
    other_loc = True
except:
    print('This address is invaild, countining with other address')
    locs = [NY, DC, NY_near]
    other_loc = False

chart = input('would you like a chart? (y/n)   ')
if chart == 'y':
    while True:
        loc = input('What loc would you like to print? (all/DC/NY Near/NY, or if it worked, ' + other_name + ' if it worked)   ')
        if loc == 'all':
            plt_display_forecast(locs, hour)
            break
        elif loc == 'DC':
            plt_display_forecast([DC], hour)
            break
        elif loc == 'NY':
            plt_display_forecast([NY], hour)
            break
        elif loc == 'NY Near':
            plt_display_forecast([NY_near], hour)
            break
        if loc == other_name:
            if other_loc == True:
                plt_display_forecast([other], hour)
                break
            else:
                print('sorry ' + other_name + ' is not working')
else:
    while True:
        loc = input('What loc would you like to print? (all/DC/NY Near/NY, or if it worked, ' + other_name + ' if it worked)   ')
        if loc == 'NY':
            NY.txt_display_forecast()
            break
        elif loc == 'DC':
            DC.txt_display_forecast()
            break
        elif loc == 'NY Near':
            NY_near.display_forecast()
            break
        if loc == other_name:
            if other_loc == True:
                plt_display_forecast([other], hour)
                break
            else:
                print('sorry ' + other_name + ' is not working')