import json
import networkx as nx
import requests
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

api_key = os.getenv("covalent_key")

host = "https://api.covalenthq.com"
# endpoint = "/v1/1/address/{address}/transfers_v2/?contract-address={contract_address}&key={API_KEY}"

G = nx.MultiDiGraph()
G.add_node("0x712d0f306956a6a4b4f9319ad9b9de48c5345996")

FTX_ADDRESS = '0x2FAF487A4414Fe77e2327F0bf4AE2a264a776AD2'

df = pd.DataFrame(columns=['tx_hash', 'from_address', 'to_address','transfer_type', 'delta'])  

def get_parent(myaddress, count):

    # if(myaddress == FTX_ADDRESS or count >= 5):
    #     return

    endpoint = "/v1/1/address/{address}/transfers_v2/?contract-address=0x50D1c9771902476076eCFc8B2A83Ad6b9355a4c9&key={API_KEY}"

    print("starting json stuff")
    
    try:
        endpoint = endpoint.format(address = myaddress, API_KEY = api_key)
        newrequest = requests.get(host+endpoint)
        new_json_data = json.loads(newrequest.text)
    
        print("json stuff done")

        mylist = []
        print(count)

        for stuff in new_json_data['data']['items']:
            if(stuff['transfers'][0]['tx_hash'] not in df['tx_hash']):
                
                mylist.append(stuff['transfers'][0]['from_address'])

                df.loc[len(df.index)] = [stuff['transfers'][0]['tx_hash'],stuff['transfers'][0]['from_address'], stuff['transfers'][0]['to_address'], stuff['transfers'][0]['transfer_type'],stuff['transfers'][0]['delta']]

        for ad in mylist:
            get_parent(ad, count+1)

    except:
        print(f"Json stuff failed as address was {myaddress}")



# json_data_str = json.dumps(json_data, indent = 2)

get_parent("0x712d0f306956a6a4b4f9319ad9b9de48c5345996", 0)
df.to_csv('file1.csv')

# endpoint = "/v1/1/address/{address}/transfers_v2/?contract-address=0x50D1c9771902476076eCFc8B2A83Ad6b9355a4c9&key={API_KEY}"

# endpoint = endpoint.format(address = "0x79ebd6ca9f685e10ec9f9e205c4f7e685dae8c73", API_KEY = api_key)
# newrequest = requests.get(host+endpoint)
# new_json_data = json.loads(newrequest.text)

# print("json stuff done")

# for stuff in new_json_data['data']['items']:
#     if(stuff['transfers'][0]['tx_hash'] not in df['tx_hash']):
#         df.loc[len(df.index)] = [stuff['transfers'][0]['tx_hash'],stuff['transfers'][0]['from_address'], stuff['transfers'][0]['to_address'], stuff['transfers'][0]['transfer_type'],stuff['transfers'][0]['delta']]
#         print(stuff['transfers'][0]['tx_hash'])


print(df)





