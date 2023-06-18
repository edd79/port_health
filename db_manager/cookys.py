import requests

response = requests.get('http://127.0.0.1:8000/')
csrftoken = response.cookies['csrftoken']
url = 'http://127.0.0.1:8000/patient'
headers = {'X-CSRFToken': csrftoken}