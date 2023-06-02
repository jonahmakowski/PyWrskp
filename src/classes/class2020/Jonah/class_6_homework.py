import requests
# get the weather of the white house
street = '1600+Pennsylvania+Avenue+NW'
city = 'Washington'
state = 'DC'
zipcode = "20500"
geocode = requests.get("https://geocoding.geo.census.gov/geocoder/locations/address?street={}&city={}&state={}&zip={}&benchmark=4&format=json".format(street, city, state, zipcode))

coordinates = geocode.json()['result']['addressMatches'][0]['coordinates']

gridpoints = requests.get('https://api.weather.gov/points/{},{}'.format(coordinates['y'], coordinates['x']))

forecast = requests.get(gridpoints.json()['properties']['forecastHourly'])

# print(forecast.text) # uncomment to print raw forecast info


pl = input('Would you like a chart? (y/n)   ')

if pl == 'y':
    pl = True
else:
    pl = False


time = str(forecast.json()['properties']['periods'][0]['startTime'])
time = time[-5:]
hour = int(time[:-3])
tick = 0
if not pl:
    for hr in forecast.json()['properties']['periods']:
        time = str(hour) + ':00'
        print('{} {}, {} \n{} \n\n'.format(time, hr['temperature'], hr['temperatureUnit'], hr['shortForecast']))
        hour += 1
        if hour == 25:
            hour = 1
        tick += 1
        if tick == 24:
            break
if pl:
    import matplotlib.pyplot as plt
    times, temp = [], []
    for hr in forecast.json()['properties']['periods']:
        time = str(hour) + ':00'
        times.append(time)
        temp.append(hr['temperature'])
        hour += 1
        if hour == 25:
            hour = 1
        tick += 1
        if tick == 24:
            break
    fig = plt.figure()
    fig.set_figheight(10)
    fig.set_figwidth(15)
    plt.plot(times, temp, 'o-')
    plt.gcf().autofmt_xdate()
    plt.grid()
    plt.show()