import requests, os 
import pprint
import inquirer
from inquirer.themes import GreenPassion
from reg import getDropletiP
pp = pprint.PrettyPrinter(indent=4)

do_dropl_url = "https://api.digitalocean.com/v2/droplets"

api_key = os.getenv("API_DIGIT")
headers = {'Content-Type': 'application/json',
           'Authorization':f'Bearer {api_key}'}
# response = requests.get(url=do_dropl_url, headers=headers)
# # response_json = response.json()
# # pprint(response_json) 




req = {
  "name": "Server1",
  "region": "nyc3",
  "size": "s-1vcpu-1gb",
  "image": "centos-stream-8-x64",
  "ssh_keys": "40889740",
}

question = [
     inquirer.Text("name", message="Whats your name?", default=""),
]
selected = inquirer.prompt(question, theme=GreenPassion())

req["name"]= selected['name']
print(req['name'])
question = [
    inquirer.List("regions", message="What is your region?", choices=getDropletiP(), default="None"),
]
reg_chous = inquirer.prompt(question, theme=GreenPassion())
print(reg_chous)
req['region']= reg_chous['regions']
print (req)

# print(f"You've selected {selected}")

# def getDropletiP(dropletID):
#     response = requests.get(url=do_dropl_url, headers=headers)
#     response_json = response.json()
#     for i in response_json["ssh_keys"]:
#         if i['name'] == 'khusravnazarov@Khusravs-MBP':
#             ssh_id = i['id']
#             print(ssh_id)
            
#     # return ssh_id
#             # if g["name"] == "khusravnazarov@Khusravs-MBP"
#             #     pprint (g["id"])
#     # pprint (response_json)
#     # for i in response_json["droplets"]:
#     #     pprint(droplets)
        
#         # if i['id'] == dropletID:  
            
#         #     pprint(i["networks"])    
            
            
# getDropletiP(407740735)