import requests
import json

Mac_Add = input("Enter The Mac Address  ")
Url = "https://api.macaddress.io/v1?apiKey=at_Xv2Z6uVSr0a5O045KtgDw2F0Ri5gQ&output=json"
params={"search": Mac_Add}
payload= {}
headers= {}

response = requests.request("GET", Url,params=params, headers=headers, data = payload)
status_code = response.status_code
content = json.loads(response.content)
#print(status_code)
#print (json.dumps(content, indent=2))
if(status_code==200):
	print(content['vendorDetails']['companyName'])
else:
	print('Irregular Input')