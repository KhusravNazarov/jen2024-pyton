import requests, os 
import pprint

pp = pprint.PrettyPrinter(indent=4)

do_dropl_url = "https://api.digitalocean.com/v2/account/keys"

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
def getDropletiP(dropletID):
    response = requests.get(url=do_dropl_url, headers=headers)
    response_json = response.json()
    for i in response_json["ssh_keys"]:
        if i['name'] == 'khusravnazarov@Khusravs-MBP':
            ssh_id = i['id']
            print(ssh_id)
            
    # return ssh_id
            # if g["name"] == "khusravnazarov@Khusravs-MBP"
            #     pprint (g["id"])
    # pprint (response_json)
    # for i in response_json["droplets"]:
    #     pprint(droplets)
        
        # if i['id'] == dropletID:  
            
        #     pprint(i["networks"])    
            
            
getDropletiP(407740735)