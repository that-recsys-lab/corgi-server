import requests
import webbrowser
import dotenv
import os
import json
import datetime

dotenv.load_dotenv()

client_key = os.getenv('CLIENT_KEY')
client_secret = os.getenv('CLIENT_SECRET')

redirect_uri = 'urn:ietf:wg:oauth:2.0:oob'
scope = 'read write push'
mastodon_instance_url = 'https://hci.social'

def getAuthCode():
    auth_url = f"https://hci.social/oauth/authorize?client_id={client_key}&redirect_uri={redirect_uri}&scopes={scope}&response_type=code"
    webbrowser.open(auth_url)

def getToken(authorization_code):

    endpoint = f'{mastodon_instance_url}/oauth/token'
    data = {
        'client_id': client_key,
        'client_secret': client_secret,
        'grant_type': 'authorization_code',
        'code': authorization_code,
        'redirect_uri': redirect_uri
    }

    response = requests.post(endpoint, data=data)
    print(response.json())

def getTimeline(access_token):
    endpoint = f'{mastodon_instance_url}/api/v1/timelines/home'
    params = {
        'limit': 40,          
    }
    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    response = requests.get(endpoint, params=params, headers=headers)
    if response.status_code == 200:
        print('SUCCESS')
        data = response.json()
        filename = 'home_timeline.json' + datetime.now()
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    else:
        print(response.json())
    

#call this to get the auth code, then set it
getAuthCode()
authorization_code = ''

#then pass the code to get the token
getToken(authorization_code=authorization_code)
token = ''

getTimeline(token)
