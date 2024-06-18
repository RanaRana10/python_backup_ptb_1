'''
This code will make some database
'''


from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

db_location = f"db_04_april.db"
engine = create_engine(f"sqlite+pysqlite:///{db_location}", echo=False)

Base = declarative_base()


class User(Base):
    __tablename__ = "my_user"

    id_ = Column(Integer, primary_key=True)
    user_id_ = Column(Integer)
    username_ = Column(String)
    token_ = Column(Integer)
    type_ = Column(String)
    expires_date_ = Column(Integer)

    def __init__(self,
                 user_id_ : int,
                 username_ : str,
                 token_ : int,
                 type_ : str,
                 expires_date_ : str):

        self.user_id_ = user_id_
        self.username_ = username_
        self.token_ = token_
        self.type_ = type_
        self.expires_date_ = expires_date_
        self.expires
