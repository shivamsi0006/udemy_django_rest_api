import requests

# http://127.0.0.1:8000/api/updates/3/

BASE_URL="http://127.0.0.1:8000/"

ENDPOINT="api/updates"

def get_list():
    r= requests.get(BASE_URL+ENDPOINT)
    return r.json()

get_list()
