import requests, json

data = {
        'firstName' : 'hello',
        'lastName' : 'world',
        'email' : 'hello12@world.com',
        'password' : 'password', 
        'active' : True,
        'created_at' : '',
        'updated_at' : '',
        'last_connection': ''
    }

headers = {
    'accept': 'application/ld+json',
    'Content-Type': 'application/ld+json',
}
# create new user with the form data. Hash the password so plaintext version isn't saved.
res = requests.post('http://localhost:9000/api/users', headers=headers, json=data)

print(res.text)