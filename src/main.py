from etl_bitcoin import extract_data_bitcoin, transform_data_bitcoin
from database import engine, sessionmaker, BitcoinPrice
from datetime import datetime
from time import sleep

def save_bitcoin_data():
    raw_data = extract_data_bitcoin()
    transformed = transform_data_bitcoin(raw_data)
    
    session = sessionmaker(bind=engine)
    session = session()

    bitcoin = BitcoinPrice(price = float(transformed['price']),
                           cryptocoin = transformed['cryptocoin'],
                           coin = transformed['coin'],
                           timestamp = datetime.fromtimestamp(transformed['timestamp']))
    
    session.add(bitcoin)
    session.commit()
    session.close
    print(f'Data Saved on {datetime.now().replace(microsecond=0)}')


def main():
    while True:
        try:
            save_bitcoin_data()
        except Exception as error_data:
            print(f'Error Data Save: {error_data}')
                  
        sleep(3600)
        

if __name__ == '__main__':
    main()

