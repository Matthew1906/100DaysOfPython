# Get Data from Trivia Database

# Import Modules
import requests 

# API Parameters
params = {
    'amount':10,
    'type':'boolean'
}

# GET from Trivia Database, and retrieve the data
questions = requests.get(url='https://opentdb.com/api.php', params=params)
questions.raise_for_status()
question_data = questions.json()['results']