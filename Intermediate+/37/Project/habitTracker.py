# DAY 37 PROJECT OF 100 DAYS OF CODE
# PROJECT NAME: HABIT TRACKER APP
# THINGS I IMPLEMENTED: API, DATETIME, REQUESTS

import requests, datetime as dt

# Uses Pixela API 
pixela_url = 'https://pixe.la/'

# 1. Create a user
# pixela_user = pixela_url+'v1/users'
# user_params = {
#     'token':'token',
#     'username':'username',
#     'agreeTermsOfService':'yes',
#     'notMinor':'yes',
# }
# we send the piece of data in json (comment it because it's already added)
# response = requests.post(url=pixela_url, json=user_params)
# Print the text
# print(response.text)

# 2. Create a Graph
graph_url = pixela_url+'v1/users/username/graphs/id'

# Header -> contains relevant pieces of information
graph_headers = {    
    'X-USER-TOKEN':'tokem'
}
graph_params = {
    # 'id':"id",
    'name':'Cyber Security Study Hours',
    'unit':'hours',
    # 'type':'int',
    # 'color':'shibafu',
}

# Commented too because already made
# graph_response = requests.put(url=graph_url, headers=graph_headers, json=graph_params)
# print(graph_response.text)

# link to graph: https://pixe.la/v1/users/username/graphs/graphid.html

# Add a value
value_url = pixela_url+'v1/users/username/graphs/graphid'
value_params = {
    'date': dt.datetime.now().strftime("%Y%m%d"),
    'quantity':'1',
}

# response = requests.post(url = value_url, headers=graph_headers, json = value_params)
# print(response.text)

# update_url = pixela_url+'v1/users/username/graphs/graphname'+ dt.datetime.now().strftime("%Y%m%d")
# Use put and delete to edit
update_params = {
    'quantity': '0'
}
# response = requests.put(url=update_url, json=update_params, headers = graph_headers)
# print(response.text)