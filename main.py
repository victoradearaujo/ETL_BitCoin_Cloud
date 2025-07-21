from etl_bitcoin import extract_data_bitcoin, transform_data_bitcoin
from database import engine, sessionmaker, BitcoinPrice
from datetime import datetime

def main():
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
    print('Data Saved')

if __name__ == '__main__':
    main()

