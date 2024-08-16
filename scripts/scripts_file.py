import requests

# http://127.0.0.1:8000/api/updates/3/

BASE_URL="http://127.0.0.1:8000/"

ENDPOINT="api/updates/"

def get_list():
    r= requests.get(BASE_URL+ENDPOINT)
    return r.json()

# get_list()


def create_update():
    message={
        "user":2,
        'id':2,
        "content":"some new data",
        "new_image":"new image"
    }
    r=requests.post(BASE_URL+ENDPOINT+"1/",data=message)
    print(r.status_code)
    if r.status_code==requests.codes.ok:
        return r.json()
    return r.status_code
        

print(create_update())

# def update_api():
#     message={
#         "user":1,
#         "id":2,
#         "content":"updated content api "
#     }

#     r=requests.put(BASE_URL+ENDPOINT,data=message)
#     return r.text

# print(update_api())