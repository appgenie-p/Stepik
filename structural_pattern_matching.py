# Get random user from randomuser.me API

import json

import requests

# Get random user from randomuser.me API


def get_random_user():
    url = 'https://randomuser.me/api/'
    response = requests.get(url)
    data = json.loads(response.text)
    # return data only if data is not empty
    if data:
        return data


if __name__ == '__main__':
    user = get_random_user()
    print(user)
