import requests
import json

#GET
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
status = 'available'

res = requests.get( f"https://petstore.swagger.io/v2/pet/findByStatus?status={status}", headers = {'accept': 'application/json'})

print(res.status_code)
print(res.json())

#POST
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
url = 'https://petstore.swagger.io/v2/pet'

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}

data = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
data = json.dumps(data)
res1 = requests.post(url, headers=headers, data=data)

print(res1.status_code)
print(res1.json())

#DELETE
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
pet_id = res1.json()['id']

url = f'https://petstore.swagger.io/v2/pet/{pet_id}'

headers = {
    'accept': 'application/json',
}

res2 = requests.delete(url, headers=headers)

print(res2.status_code)
print(res2.json())

#PUT
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
url = 'https://petstore.swagger.io/v2/pet'

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}

data = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
data = json.dumps(data)
res3 = requests.put(url, headers=headers, data=data)

print(res3.status_code)
print(res3.json())