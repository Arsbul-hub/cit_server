import os.path

import requests
import os
if not os.path.isfile("token.txt"):
    f = open("token.txt", "w")
    f.close()
with open("token.txt", "r") as f:
    d = f.read()
    if d:
        token = d

    else:
        register_data = requests.post("http://127.0.0.1:5000/register",
                                      json={"username": "Test1211", "password": "test"}).json()
        print(register_data)
        token = register_data["token"]
        with open("token.txt", "w") as f:
            f.write(token)


# d = requests.post("http://127.0.0.1:5000/click",
#                                       json={"username": "arsbul", "token": token}).json()
# print(d)

d = requests.get("http://127.0.0.1:5000/get_account_data", params={"username": "Test1211", "token": token}).text
print(d)