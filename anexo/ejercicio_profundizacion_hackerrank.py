


import json
import requests
import re
import matplotlib.pyplot as plt

def fetch(page_number, location_id):
    url = "https://jsonmock.hackerrank.com/api/transactions/search?txnType=debit&page={}".format(page_number)
    
    response = requests.get(url)
    dataset = response.json()
    json_response = dataset["data"]

    filtrado = [{"userId": x["userId"] , "amount": x["amount"]} for x in json_response if x["location"]["id"] == location_id]
   
    
    return filtrado

def transform(dataset):

    data = {}

    

    for i in range(len(dataset)):
       

        variable = dataset[i]
        userid = variable['userId']
        amount = variable['amount']
        #amount = float(re.sub(r'[^\d\-.]', '', amount_str))

        if (userid in dataset ) == False:
            data[i] = 0
        data[userid] =  data[userid] #+ amount
        
        print(data)



    lista_str = json.dumps(dataset)
    amount = float(re.sub(r'[^\d\-.]', '', amount_str))

    print (lista_str)

if __name__ == "__main__":
    page_number = 1
    location_id = 7
    dataset = fetch(page_number, location_id)
    
    
    data = transform(dataset)
    #report(data)




