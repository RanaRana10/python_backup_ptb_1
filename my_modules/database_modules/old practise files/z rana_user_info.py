'''
This code will make some database
'''

from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker

from datetime import datetime, timedelta


# db folder = Path()

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
    last_starting_time_ = Column(DateTime)
    expires_date_ = Column(DateTime)
    expires_date_int_ = Column(Integer)

    def __init__(self,
                 user_id_: int = 000_000_0000,
                 username_: str = None,
                 token_: int = None,
                 type_: str = None,
                 last_starting_time_: datetime = None,
                 expires_date_: datetime = datetime(1,1,1,12,0,0),
                 expires_date_int_: int = None,
                 ):

        self.user_id_ = user_id_
        self.username_ = username_
        self.token_ = token_ 
        self.type_ = type_
        self.last_starting_time_ = last_starting_time_
        self.expires_date_ = expires_date_
        self.expires_date_int_ = expires_date_int_

    def __repr__(self):
        f"This is the Table of User information store"


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


def main():
    # user1 = User(
    #     user_id_=123,
    #     username_="abc",
    #     token_=34,
    #     type_="a",
    #     expires_date_int_=171224023787,
    #     expires_date_=datetime(year = 2024,day = 12, month = 9)
    #     )

    user2 = User(
        user_id_=222,
        # username_="abcaa",
        username_= False,
        token_=343,
        type_="a",
        expires_date_int_=171224023787,
        expires_date_=datetime(year=2024, day=12, month=9)
    )

    session.add(user2)
    session.commit()


if __name__ == "__main__":
    main()
