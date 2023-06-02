import requests
# get the weather of the white house
street = '1600+Pennsylvania+Avenue+NW'
city = 'Washington'
state = 'DC'
zipcode = "20500"
geocode = requests.get("https://geocoding.geo.census.gov/geocoder/locations/address?street={}&city={}&state={}&zip={}&benchmark=4&format=json".format(street, city, state, zipcode))

coordinates = geocode.json()['result']['addressMatches'][0]['coordinates']

gridpoints = requests.get('https://api.weather.gov/points/{},{}'.format(coordinates['y'], coordinates['x']))

forecast = requests.get(gridpoints.json()['properties']['forecast'])

# print(forecast.text) # uncomment to print raw forecast info
for days in forecast.json()['properties']['periods']:
    print('{}:\n{}{}, {} \n \n {} \n \n \n'.format(days['name'], days['temperature'], days['temperatureUnit'], days['shortForecast'], days['detailedForecast']))