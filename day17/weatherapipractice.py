import requests #bring this to request url

#set up a suitable url that can run the darksky api
endpoint = "https://api.darksky.net/forecast/"
key = "1ba105847feda2c827b8171277ef4c11"
lat = input('latitude? ')
lon = input('longitude? ')


#combine all the elements to make a url
url = endpoint + key + '/' + lat + ',' + lon + "?units=si"

#request the data from the url
r = requests.get(url)
print(r)

#take the data and label it weather, making sure it it is in .json
weather = r.json()

#create a forecast that tells all the relevant information in the dictionary
forecast =  "It\'s currently %s degrees. Expect there to be %s humidity. Also, windspeed is %s, so take notice when you are at %s latitude, %s longitude. Expect there to be have " % (weather['currently']['temperature'], weather['currently']['humidity'], weather['currently']['windSpeed'], lat, lon)
print(forecast)
