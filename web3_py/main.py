#copied from https://www.quicknode.com/guides/web3-sdks/how-to-generate-a-new-ethereum-address-in-python

from eth_account import Account
import secrets
import json
import requests
import time
#TODO - run multiple times
priv = secrets.token_hex(32)
private_key = "0x" + priv
print ("SAVE BUT DO NOT SHARE THIS:", private_key)
acct = Account.from_key(private_key)
print("Address:", acct.address)



#using etherscan api: 
#sample call to get amount for address: /api?module=account&action=balance&address=0xddbd2b932c763ba5b1b7ae3b362eac3e8d40121a&tag=latest&apikey=YourApiKeyToken
address = acct.address
api_token = 'CPEIY7AV716GYVHQ49IM5X6A1IGW8I23YD'
url = 'https://api.etherscan.io/api?module=account&action=balance&address=' + address + '&tag=latest&apikey=' + api_token
r = requests.get(url)
json_resp = json.loads(r.text)
try:
    print(r.text)
    print(json_resp)
except:
    print("oops an exception")

