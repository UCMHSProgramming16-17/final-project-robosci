import requests

endpoint = "https://api.darksky.net/forecast/"
key = "1ba105847feda2c827b8171277ef4c11"
lat = input('latitude? ')
lon = input('longitude? ')

url = endpoint + key + '/' + lat + ',' + lon + "?units=si" #gives in si units
print(url)

payload = {'exclude'}

r = requests.get(url, params = payload)
print(r)
print(r.url)

weather = r.json()

forecast =  "It\'s currently %s degrees at %s latitude, %s longitude. E" % (weather['currently']['temperature'], lat, lon)
print(forecast)