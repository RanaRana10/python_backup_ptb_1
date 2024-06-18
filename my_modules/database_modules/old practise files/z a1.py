from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

db_location = f"practise_db.db"
engine = create_engine(f"sqlite+pysqlite:///{db_location}", echo= False)
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key= True)
    username = Column(String, nullable= False, unique= True)
    email = Column(String, nullable= False)

    def __init__(self, username, email):
        self.username = username
        self.email = email

Base.metadata.create_all(engine)
Session = sessionmaker(bind = engine)
session = Session()

user3 = User("mallppo", ".dflkj")


try:
    session.add(user3)
    session.commit()

except Exception as e:
    print("failed")

session.close()













































