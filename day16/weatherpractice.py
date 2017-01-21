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

forecast =  "It\'s currently %s degrees. Expect there to be %s % humidity. Also, windspeed is %s, so take notice when you are at %s latitude, %s longitude. Expect there to be have " % (weather['currently']['temperature'], weather['currently']['humidity'], weather['currently']['windSpeed'], lat, lon)
print(forecast)