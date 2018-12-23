# for more information on how to install requests
# http://docs.python-requests.org/en/master/user/install/#install
import requests
import json

# TODO: replace with your own app_id and app_key
app_id = '2bce5031'
app_key = '920201819850ccfc00368666b48ebaa6'

language = 'en'
def oxford():

    word_id = input("Enter the word to search it's meaning: ")

    url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' +  word_id.lower()

    r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})

    print(r.text)

    
