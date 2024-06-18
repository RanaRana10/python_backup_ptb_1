'''
This module is for store the User data insert into my database
i need to import session which will to use like, add, qurey and so on
'''
from datetime import datetime, timedelta
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker

db_location = f"user_data_5_april.db"
engine = create_engine(f"sqlite + pysqlite:///{db_location}", echo = False)

Base = declarative_base()


class User(Base):
    __tablename__ = "users_details"

    id_ = Column(Integer, primary_key = True)
    user_id_ = Column(Integer)
    user_name_ = Column(String)
    full_name_ = Column(String)
    first_time_ = Column(DateTime)
    type_ = Column(String)
    token_ = Column(Integer)
    valid_until_ = Column(DateTime)
    extra_1_ = Column(String)
    extra_2_ = Column(String)
    extra_3_ = Column(String)


    def __init__(self,
                 user_id_: int = 000,
                 user_name_: str = None,
                 full_name_: str = None,
                 first_time_: datetime = None,
                 type_: str = None,
                 token_: int = None,
                 valid_until_: datetime = None,
                 extra_1_: str = None,
                 extra_2_: str = None,
                 extra_3_: str = None,
                 ):
        
        self.user_id_ = user_id_
        self.user_name_ = user_name_
        self.full_name_ = full_name_
        self.first_time_ = first_time_
        self.type_ = type_
        self.token_ = token_
        self.valid_until_ = valid_until_
        self.extra_1_ = extra_1_
        self.extra_2_ = extra_2_
        self.extra_3_ = extra_3_
        
    def __repr__(self):
        return f"The information is: \n<User(id={self.id_}, user_name={self.user_name_}, full_name={self.full_name_})>"



Base.metadata.create_all(engine)
Session = sessionmaker(bind= engine)
session = Session()













































