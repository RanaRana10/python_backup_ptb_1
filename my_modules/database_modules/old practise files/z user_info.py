'''
This code will make some database
'''


from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime
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
    expires_date_ = Column(DateTime)
    expires_date_int_ = Column(Integer)

    def __init__(self,
                 user_id_: int,
                 username_: str,
                 token_: int,
                 type_: str,
                 expires_date_,
                 expires_date_int_: int,
                 ):

        self.user_id_ = user_id_
        self.username_ = username_
        self.token_ = token_
        self.type_ = type_
        self.expires_date_ = expires_date_
        self.expires_date_int_ = expires_date_int_

    def __repr__(self):
        return f"<User(id={self.id_}, username={self.username_}, token={self.token_}, type={self.type_})>"



Base.metadata.create_all(engine)
Session = sessionmaker(bind= engine)
session = Session()


def main():
    user1 = User(123,"abc", 34, "a", 1712240237)
    session.add(user1)
    session.commit()



if __name__ == "__main__":
    main()
