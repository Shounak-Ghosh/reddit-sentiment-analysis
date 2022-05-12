import requests

# note that CLIENT_ID refers to 'personal use script' and SECRET_TOKEN to 'token'
auth = requests.auth.HTTPBasicAuth(
    'mzLs0S9lRAjFbFQ1X7yukg', 'QkZtRMVz6Gayrf2K4iTVu-ini4-Npg')

# here we pass our login method (password), username, and password
data = {'grant_type': 'password',
        'username': 'RevolutionaryHat4034',
        'password': 'FndqrUQk7s5Cztj'}

# setup our header info, which gives reddit a brief description of our app
headers = {'User-Agent': 'sentiment-analysis/0.0.1'}

# send our request for an OAuth token
res = requests.post('https://www.reddit.com/api/v1/access_token',
                    auth=auth, data=data, headers=headers)

# convert response to JSON and pull access_token value
TOKEN = res.json()['access_token']

# add authorization to our headers dictionary
headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}

# while the token is valid (~2 hours) we just add headers=headers to our requests
requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)


