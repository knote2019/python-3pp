import json
import requests

user1 = dict()
user1.update({'username': 'kenny1'})
user1.update({'password': 'pass11'})

if __name__ == "__main__":

    url = "http://localhost:8989/notifier/subscriber"

    jsonstr = json.dumps(user1)

    requests.post(url,
                  data=jsonstr,
                  headers={'Content-Type': 'application/json'})

    requests.put(url,
                 data=jsonstr,
                 headers={'Content-Type': 'application/json'})

    req = requests.get(url + '/1',
                       headers={'Content-Type': 'application/json'})
    print(req.json())

    req = requests.delete(url + '/1',
                          headers={'Content-Type': 'application/json'})
    print(req.json())
