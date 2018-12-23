import requests
import json
import urllib
import pprint
url = 'https://api.stackexchange.com/2.2/search/advanced'
def stack_apps_api():
    query_tag = input("Add a tag to the query: ")
    query_title = input("Input the query consicely: ")    
    payload = {
        'order': 'desc',
        'sort': 'activity',
        'tagged': query_tag,
        'title': query_title,
        'site': 'stackoverflow',
        'filter': 'withbody',
        }
    r = requests.get("https://api.stackexchange.com/2.2/search/advanced", params = payload) 
    data = r.json()
    number_of_responses = len(data['items'])
    if number_of_responses == 0:
        print("No response for the entered input")
        return
    for i in data['items']:
        print('Tags: ', i['tags'])
        print('Title: ',i['title'] )
        print('Link: ', i['link'])
        question_id = i['question_id']
        pprint.PrettyPrinter(width=41, compact=True).pprint('Question: '+ i['body'])
        print('_'*20)
        payload_answer = {
            'order': 'desc',
            'sort': 'activity',
            'site': 'stackoverflow',
            'filter': 'withbody',}
        answer_r = requests.get(f"https://api.stackexchange.com/2.2/questions/{question_id}/answers", params = payload_answer)
        answer = answer_r.json()
        if len(answer['items']) == 0:
            print("No response")
            return
        for i in answer['items']:
            print("Is answer accepted: ", i['is_accepted'])
            print("Answer: ", i['body'])
            print("*" * 20)

        print("#" * 20)     
#stack_apps_api()

