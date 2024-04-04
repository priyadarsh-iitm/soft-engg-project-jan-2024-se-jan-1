from application.api import *
import json

def auth_token():
    return "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoyMCwiZXhwIjoxNzEyMjMzODA3fQ.kAWSWKVOoWWYnThDOm_4ZMYk0d-NUpimH7x0xAQ8uPs"

def auth_user_token():
    return  "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoyNiwiZXhwIjoxNzEyMjM4MjYwfQ.6vDvTIZkLDj9wUoTbjEfxiGfPNgtkgbbHmCEaUrUF24"

var = 'Newtest4'
ticket_id = 7
# def test_user_admin_post():

#     header = {'secret_authtoken':auth_token(), "Content-Type":"application/json"}
#     data = {
#         "email_id":f'{var}@email.com',
#         "password":"Variable123456",
#         "role_id":1
#     }
#     data = json.dumps(data)
#     response = requests.post('http://127.0.0.1:5000/api/user',data = data,headers = header)
#     assert response.status_code==200
#     headers = {
#         'Api-Key': 'a7d557f8eccc7f587756c5038a51064b7dc1c882929c03000dab8ad013165247',
#         'Api-Username': '21f1005104',
#         'Content-Type': 'application/json'
#     }

#     response = requests.get(f"http://localhost:4200/u/{var}.json",headers = headers)
#     print(response.json())
#     r_dict = response.json()['user']
#     assert response.status_code==200
#     assert r_dict['username'] == var
#     assert r_dict['name'] == var

# def test_post_user_create():
#     header = {'secret_authtoken':auth_user_token(), "Content-Type":"application/json"}
#     payload = {
#                 "title": 'Hayeeeeee Kemcho Nameste Hola Gracias Again Welcome to new TESTING MY newwest TEST CASE USING PYTEST',
#                 "description": 'Aayeeee Bhaijan Gelo Hello Again new Pytest newest testing going on via vs code',
#                 "number_of_upvotes":0,
#                 "is_read":0,
#                 "is_open":1,
#                 "is_offensive":0,
#                 "is_FAQ":0,
#                 "creator_id":26
#                 }
    
#     payload = json.dumps(payload)
#     response = requests.post('http://127.0.0.1:5000/api/ticket',data = payload,headers=header)
#     print(response)
#     assert response.status_code==200


#     discourse_headers = {
#                 'Api-Key': 'a7d557f8eccc7f587756c5038a51064b7dc1c882929c03000dab8ad013165247',
#                 'Api-Username':"pytest1"
#             }

#     payload_dict = json.loads(payload)
#     current_ticket = db.session.query(Ticket).filter(Ticket.title==payload_dict['title'],Ticket.description==payload_dict['description']).first()
#     discourse_id = current_ticket.discourse_id
#     print(discourse_id)

#     discourse_response = requests.get(f"http://localhost:4200/t/{discourse_id}.json",headers = discourse_headers)
#     print(discourse_response.json())
#     assert discourse_response.status_code==200
    
#     res = discourse_response.json()
#     print(res)
#     assert res['title'] == payload_dict['title']
    

# def test_post_user_update():
#     payload = {
#                 "title":"New title has been made",
#                 "ticket_id":7
#             }
#     payload = json.dumps(payload)
#     header = {'secret_authtoken':auth_user_token(), "Content-Type":"application/json"}
#     response = requests.patch("http://127.0.0.1:5000/api/ticket",data = payload,headers=header)
#     assert response.status_code==200

#     discourse_headers = {
#                 'Api-Key': 'a7d557f8eccc7f587756c5038a51064b7dc1c882929c03000dab8ad013165247',
#                 'Api-Username':'pytest1'
#             }    
#     payload_dict = json.loads(payload)
#     current_ticket = db.session.query(Ticket).filter(Ticket.ticket_id==payload_dict['ticket_id']).first()
#     discourse_id = current_ticket.discourse_id
#     print(discourse_id)

#     discourse_response = requests.get(f"http://localhost:4200/t/{discourse_id}.json",headers = discourse_headers)
#     print(discourse_response.json())
#     assert discourse_response.status_code==200
    
#     res = discourse_response.json()
#     print(res)
#     assert res['title'] == payload_dict['title']


# def test_post_user_delete():
#     header = {'secret_authtoken':auth_user_token(), "Content-Type":"application/json"}
#     current_ticket = db.session.query(Ticket).filter(Ticket.ticket_id==ticket_id).first()
#     discourse_id = current_ticket.discourse_id
#     response = requests.delete(f"http://127.0.0.1:5000/api/ticket/{ticket_id}",headers=header)
#     assert response.status_code==200

#     discourse_headers = {
#                 'Api-Key': 'a7d557f8eccc7f587756c5038a51064b7dc1c882929c03000dab8ad013165247',
#                 'Api-Username':'pytest1'
#             }    

    
#     print(discourse_id)

#     discourse_response = requests.get(f"http://localhost:4200/t/{discourse_id}.json",headers = discourse_headers)
#     print(discourse_response.json())
#     assert discourse_response.json()['post_stream']['posts'][0]['can_edit']==False



# def test_user_admin_delete():
#     header = {'secret_authtoken':auth_token(), "Content-Type":"application/json"}
#     data = {
#         "user_id":25
#     }
#     current_user = User.query.filter(User.user_id==int(data['user_id'])).first()
#     print(current_user.user_name)
#     uname = current_user.user_name

#     response = requests.delete(f'http://127.0.0.1:5000/api/user/{data["user_id"]}',headers = header)
#     assert response.status_code==200

#     headers = {
#     'Api-Key': 'a7d557f8eccc7f587756c5038a51064b7dc1c882929c03000dab8ad013165247',
#     'Api-Username': '21f1005104',
#     'Content-Type': 'application/json'
#     }
#     response = requests.get(f"http://localhost:4200/u/{uname}.json",headers = headers)
#     print(response.json())
    
#     assert response.status_code==404
    
