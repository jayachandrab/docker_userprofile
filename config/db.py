from sqlalchemy import create_engine, engine,MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

print("===========",BASE_DIR)

db_url=os.environ["DATABASE_URL"]

#engine=create_engine("mysql+pymysql://root:root@localhost:3306/test")
engine=create_engine(db_url)

meta=MetaData()
conn=engine.connect()


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base=declarative_base()

