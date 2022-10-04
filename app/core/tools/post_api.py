import requests

def post_api(url, data, headers):
    response = requests.post(url, headers=headers, json=data)
    return response