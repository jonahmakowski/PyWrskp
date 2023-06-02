import requests
street = "1600+Pennsylvania+Avenue+NW"
city = "Washington"
state = "DC"
zipcode = "20500"
geocode = requests.get("https://geocoding.geo.census.gov/geocoder/locations/address?street={}&city={}&state={}&zip={}&benchmark=4&format=json".format(street, city, state, zipcode))
        #print(geocode.text)
coordinates = geocode.json()['result']['addressMatches'][0]['coordinates']
gridpoints = requests.get('https://api.weather.gov/points/{},{}'.format(coordinates['y'],coordinates['x']))
        #print(gridpoints.text)
forecast = requests.get(gridpoints.json()['properties']['forecastHourly'])