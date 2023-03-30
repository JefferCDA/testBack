from dotenv import load_dotenv
import os

load_dotenv()

hostDB = os.environ['MYSQL_HOST']
userDB = os.environ['MYSQL_USER']
passwordDB = os.environ['MYSQL_PASSWORD']
nameDB = os.environ['MYSQL_DB']
secretKey = os.environ['SECRET_KEY']

DATABASE_CONNECTION_URI = f'mysql+pymysql://{userDB}:{passwordDB}@{hostDB}/{nameDB}' 

class DevelopmentConfig():
    DEBUG = True;

Config = {
    'development' : DevelopmentConfig
}