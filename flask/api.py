import json
import connexion

user1 = dict()
user1.update({'username': 'kenny1'})
user1.update({'password': 'pass11'})

user2 = dict()
user2.update({'username': 'kenny2'})
user2.update({'password': 'pass22'})

user3 = dict()
user3.update({'username': 'kenny2'})
user3.update({'password': 'pass22'})

users = dict()

users.update({user1['username']: user1})
users.update({user2['username']: user2})
users.update({user3['username']: user3})


def create_subscriber(body):
    print('create_subscriber')
    print(body)
    if connexion.request.is_json:
        body_dict = json.dumps(connexion.request.get_json())
        print(body_dict)
    return 1, 201


def update_subscriber(body):
    print('update_subscriber')
    print(body)
    if connexion.request.is_json:
        body_dict = json.dumps(connexion.request.get_json())
        print(body_dict)
    return 1, 201


def delete_subscriber(subscriber_id):
    print('delete_subscriber')
    print(subscriber_id)
    return 1, 201


def get_subscriber(subscriber_id):
    print('get_subscriber')
    print(subscriber_id)
    return json.dumps(user1), 201
