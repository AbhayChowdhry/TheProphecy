import json
import networkx as nx
import requests
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

api_key = os.getenv("covalent_key")

host = "https://api.covalenthq.com"
endpoint = "/v1/1/address/{address}/transfers_v2/?contract-address={contract_address}&key={API_KEY}"

endpoint = endpoint.format(address = "0x20b6553032816e748ab1f3d20859c7cd485b9674", contract_address = "0x50D1c9771902476076eCFc8B2A83Ad6b9355a4c9", API_KEY = api_key)

FTX_ADDRESS = '0x2FAF487A4414Fe77e2327F0bf4AE2a264a776AD2'

# def get_parent(address):

#     if(address == ):
#         return
#     else:
#         get_parent(address) 

df = pd.DataFrame(columns=['tx_hash', 'from_address', 'to_address','transfer_type', 'delta'])  

parameters = {
    
}

request = requests.get(host+endpoint)

json_data = json.loads(request.text)
json_data_str = json.dumps(json_data, indent = 2)

list_tbi = [0, 0, 0, 0, 0]

for stuff in json_data['data']['items']:
    # print(stuff['transfers'][0]['from_address'])
    # print(stuff['transfers'][0]['to_address'])
    # print(stuff['transfers'][0]['transfer_type'])
    # print(stuff['transfers'][0]['delta'])
    # print(stuff['transfers'][0]['tx_hash'])
    tba = {
        'tx_hash':stuff['transfers'][0]['tx_hash'],
        'from_address':stuff['transfers'][0]['from_address'],
        'to_address':stuff['transfers'][0]['to_address'],
        'transfer_type':stuff['transfers'][0]['transfer_type'],
        'delta':stuff['transfers'][0]['delta'],
    }

    # print()
    # print()

    df.loc[len(df.index)] = [stuff['transfers'][0]['tx_hash'],stuff['transfers'][0]['from_address'], stuff['transfers'][0]['to_address'], stuff['transfers'][0]['transfer_type'],stuff['transfers'][0]['delta']]


print(df)





