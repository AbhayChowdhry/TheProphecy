import json
import networkx as nx
import requests
import os
from dotenv import load_dotenv
import pandas as pd
import time

# class Node:
#     def __init__(self, address, value):
#         self.address = address
#         self.value = value

load_dotenv()
api_key = os.getenv("covalent_key")
host = "https://api.covalenthq.com"

G = nx.MultiDiGraph()

FTX_ADDRESS = '0x2faf487a4414fe77e2327f0bf4ae2a264a776ad2'

df = pd.DataFrame(columns=['tx_hash', 'from_address', 'to_address','transfer_type', 'delta'])  

node_list = []

def get_parent(myaddress):

    if(myaddress == FTX_ADDRESS):
        print("REACHED LESSSGOO")
        return

    endpoint = "/v1/1/address/{address}/transfers_v2/?contract-address=0x50D1c9771902476076eCFc8B2A83Ad6b9355a4c9&key={API_KEY}"

    print("starting json stuff")
    
    try:
        endpoint = endpoint.format(address = myaddress, API_KEY = api_key)
        newrequest = requests.get(host+endpoint)
        new_json_data = json.loads(newrequest.text)
    
        print("json stuff done")

        for stuff in new_json_data['data']['items']:
            if(stuff['transfers'][0]['tx_hash'] not in df['tx_hash']):
                
                # mylist.append(stuff['transfers'][0]['from_address'])

                df.loc[len(df.index)] = [stuff['transfers'][0]['tx_hash'],stuff['transfers'][0]['from_address'], stuff['transfers'][0]['to_address'], stuff['transfers'][0]['transfer_type'],stuff['transfers'][0]['delta']]

                # if(stuff['transfers'][0]['from_address'] not in node_list):
                #     node_list.append(stuff['transfers'][0]['from_address'])
                #     G.add_node(stuff['transfers'][0]['from_address'])
                
                # if(stuff['transfers'][0]['to_address'] not in node_list):
                #     node_list.append(stuff['transfers'][0]['to_address'])
                #     G.add_node(stuff['transfers'][0]['to_address'])
                    
                # G.add_edge(stuff['transfers'][0]['from_address'], stuff['transfers'][0]['to_address'])


        # nx.draw(G)

        if(stuff['transfers'][0]['from_address'] != myaddress):
            print("Going to parent of " + stuff['transfers'][0]['from_address'])
            get_parent(stuff['transfers'][0]['from_address'])

    except:
        print(f"Json stuff failed as address was {myaddress}")



# json_data_str = json.dumps(json_data, indent = 2)

get_parent("0xc7a238f2c89371f43c99f835741459c2219bbea5")
# df.to_csv('file1.csv')





# endpoint = "/v1/1/address/{address}/transfers_v2/?contract-address=0x50D1c9771902476076eCFc8B2A83Ad6b9355a4c9&key={API_KEY}"

# endpoint = endpoint.format(address = "0x712d0f306956a6a4b4f9319ad9b9de48c5345996", API_KEY = api_key)
# newrequest = requests.get(host+endpoint)
# new_json_data = json.loads(newrequest.text)

# mylist = []

# for stuff in new_json_data['data']['items']:
#     if(stuff['transfers'][0]['tx_hash'] not in df['tx_hash']):
        
#         mylist.append(stuff['transfers'][0]['from_address'])

#         df.loc[len(df.index)] = [stuff['transfers'][0]['tx_hash'],stuff['transfers'][0]['from_address'], stuff['transfers'][0]['to_address'], stuff['transfers'][0]['transfer_type'],stuff['transfers'][0]['delta']]

#         if(stuff['transfers'][0]['from_address'] not in node_list):
#             node_list.append(stuff['transfers'][0]['from_address'])
#             G.add_node(stuff['transfers'][0]['from_address'])
        
#         if(stuff['transfers'][0]['to_address'] not in node_list):
#             node_list.append(stuff['transfers'][0]['to_address'])
#             G.add_node(stuff['transfers'][0]['to_address'])
            
#         G.add_edge(stuff['transfers'][0]['from_address'], stuff['transfers'][0]['to_address'])


# g = nx.MultiDiGraph()
# g.add_node("a")
# g.add_node("b")
# g.add_node("c")
# g.add_edge("a", "b")
# g.add_edge("c", "b")
# nx.draw(g)
# print(df)





