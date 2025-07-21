# Import Library 
from sqlalchemy import create_engine, Column, String, Float, DateTime, Integer
from sqlalchemy.orm import declarative_base, sessionmaker 
from dotenv import load_dotenv
import os 
import datetime

load_dotenv()

user = os.getenv('POSTGRES_USER')
passaword = os.getenv('POSTGRES_PASSWORD')
host = os.getenv('POSTGRES_HOST')
port = os.getenv('POSTGRES_PORT')
db_bitcoin =os.getenv('POSTGRES_DB')

database_url = (f'postgresql://{user}:{passaword}@{host}:{port}/{db_bitcoin}')

engine = create_engine(database_url)
session = sessionmaker(bind=engine)

base = declarative_base()

class BitcoinPrice(base):
    __tablename__ = 'bitcoin_price'
    id = Column(Integer, primary_key=True, autoincrement=True)
    price = Column(Float)
    cryptocoin = Column(String)
    coin = Column(String)
    timestamp = Column(DateTime)

base.metadata.create_all(engine)
session = session()





