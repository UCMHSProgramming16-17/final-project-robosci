import requests

endpoint = 'http://isithackday.com/arrpi.php?text='
text = 'The pirates of the carribean is a great movie'

url = endpoint + text

#create url
print(url)


r = requests.get(url)
print(r)

print(r.text)