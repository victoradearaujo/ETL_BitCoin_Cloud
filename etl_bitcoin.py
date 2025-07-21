import requests
from datetime import datetime

# Extract (get-api-json)
def extract_data_bitcoin():
    url = 'https://api.coinbase.com/v2/prices/spot'
    response = requests.get(url)
    data = response.json()
    return data 


# Transform
def transform_data_bitcoin(data):
    price = data['data']['amount']
    cryptocoin = data['data']['base']
    coin = data['data']['currency']
    timestamp = datetime.now().timestamp()

    data_transform = {
        'price': price,
        'cryptocoin': cryptocoin,
        'coin': coin,
        'timestamp': timestamp
    }

    return data_transform

if __name__ == '__main__':
    # Data Extract 
    data_json = extract_data_bitcoin()
    data_result = transform_data_bitcoin(data_json)
    print(data_result)







