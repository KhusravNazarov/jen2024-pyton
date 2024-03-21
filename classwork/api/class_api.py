import requests, os 
import pprint
import inquirer
from inquirer.themes import GreenPassion

pp = pprint.PrettyPrinter(indent=4)

do_dropl_url = "https://api.digitalocean.com/v2/images"

api_key = os.getenv("API_DIGIT")
headers = {'Content-Type': 'application/json',
           'Authorization':f'Bearer {api_key}'}
# response = requests.get(url=do_dropl_url, headers=headers)
# # response_json = response.json()
# # pprint(response_json) 




# req = {
#   "name": "Server1",
#   "region": "nyc3",
#   "size": "s-1vcpu-1gb",
#   "image": "centos-stream-8-x64",
#   "ssh_keys": "40889740",
# }
# response = requests.post(url=do_dropl_url, json=req, headers=headers)
# pprint(response.json())

def getDropletiP():
    image_list = []
    response = requests.get(url=do_dropl_url, headers=headers)
    response_json = response.json()['images']
    for image in response_json:
        image_list.append(image['description'])
    print(image_list)
getDropletiP()