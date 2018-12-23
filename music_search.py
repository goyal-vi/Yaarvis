import requests
import json

url = 'https://api.stackexchange.com/2.2/search?'
response = requests.get(url, headers = {'order': 'desc' , 'sort':'activity', 'tagged': 'python', 'intitle': 'trouble installing pyaudio' })
print(response)
