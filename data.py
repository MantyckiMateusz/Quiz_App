import requests
from html import unescape

class Data:

    #Parameters for api call
    params = {
        'amount': 10,
        'type': 'boolean',
    }

    def __init__(self):
        response = requests.get('https://opentdb.com/api.php', params=self.params)
        response.raise_for_status()

        #Save the question from api call as a dictionary with only question text and the correct answer
        self.questions = [ {'question': unescape(i['question']), 'answer': i['correct_answer']} for i in response.json()['results']]

