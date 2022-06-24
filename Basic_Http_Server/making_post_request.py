import requests
import json
import time

data={
    "eno": "103", 
    "ename": "AlwaysRika", 
    "esal": "70000",
    "eaddr": "Banglore-HSR"}

def post_req():
    resp=requests.post("http://localhost:8092/",data=json.dumps(data))
    return resp.text

def get_req():
    resp=requests.get("http://localhost:8092/")
    return resp.text

if __name__ == "__main__":
    # print(post_req())
    # time.sleep(10)
    print(get_req())