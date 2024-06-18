'''
This module is for store the User data insert into my database
i need to import session which will to use like, add, qurey and so on
'''
from datetime import datetime, timedelta
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker

# db_location = f"user_data_5_april.db"
# engine = create_engine(f"sqlite+pysqlite:///{db_location}", echo=False)




db_filename = "user_information.db"
folder_name = Path("files_and_media") / "data_store_folder"
folder_name.mkdir(parents= True, exist_ok= True)
file_location = folder_name / db_filename
file_url = f"sqlite+pysqlite:///{file_location}"

engine = create_engine(url= file_url, echo= False)



Base = declarative_base()


class User(Base):
    __tablename__ = "users_details"

    id_ = Column(Integer, primary_key=True)
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

Session = sessionmaker(bind= engine)
session = Session()

def create_tables():
    '''This is essentil to create the .db file at first of the script'''
    # print(f"This Database File will create")
    Base.metadata.create_all(engine)
    # print(f"Database File has been Created")




def add_user_to_db(user_id: int, user_name: str, full_name: str, first_time: datetime, user_type:str, token: int, valid_until:datetime,extra_1=None, extra_2=None, extra_3=None):
    '''Give the information of the parameters and it will reate the obj, and then add and then commit'''

    new_user = User(user_id_=user_id, user_name_=user_name, full_name_=full_name,
                    first_time_=first_time, type_=user_type, token_=token,
                    valid_until_=valid_until, extra_1_=extra_1, extra_2_=extra_2, extra_3_=extra_3)
    session.add(new_user)
    session.commit()
    session.close()
    print("User added successfully.")


def add_user_and_return_id(user_id_: int = 000,
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
    '''This is a fun to store the information into the db and returns the file'''
    
    new_user = User(user_id_=user_id_, user_name_=user_name_, full_name_=full_name_,
                    first_time_=first_time_, type_=type_, token_=token_,
                    valid_until_=valid_until_, extra_1_=extra_1_, extra_2_=extra_2_, extra_3_=extra_3_)
    session.add(new_user)
    session.commit()
    inserted_id = new_user.id_  # get ID of the inserted row
    session.close()
    print("User added successfully. ID:", inserted_id)
    return inserted_id



def check_user_existence_by_user_id(user_id: int):
    '''Check if a user exists in the database based on user_id and it will return the id row value'''
    existing_user = session.query(User).filter(User.user_id_ == user_id).first()
    if existing_user:
        return existing_user.id_
    else:
        return None


def get_user_by_id(user_id: int):
    '''Get a user from the database based on its ID
    It will return the User obj and you can use like,
    get_user_by_id.column name to get the result
    '''
    user = session.query(User).filter(User.user_id_ == user_id).first()
    session.close()
    return user


def update_user_data_1(user_id: int, **kwargs):
    '''Update user data based on user_id'''
    user = session.query(User).filter(User.user_id_ == user_id).first()
    if user:
        for key, value in kwargs.items():
            setattr(user, key, value)
        session.commit()
        print("User data updated successfully.")
    else:
        print("User not found.")


def update_user_data_2(user_id: int, **kwargs):
    '''Update user data based on user_id'''
    user = session.query(User).filter(User.user_id_ == user_id).first()
    if user:
        for key, value in kwargs.items():
            if hasattr(User, key):
                setattr(user, key, value)
            else:
                print(f"Ignoring unknown attribute: {key}")
        session.commit()
        print("User data updated successfully.")
    else:
        print("User not found.")


def update_user_data_3(user_id: int, **kwargs):
    '''Update user data based on user_id'''
    user = session.query(User).filter(User.user_id_ == user_id).first()
    if user:
        updated_attributes = {}
        for key, value in kwargs.items():
            if hasattr(User, key):
                setattr(user, key, value)
                updated_attributes[key] = "Updated"
            else:
                updated_attributes[key] = "Ignored - Not a valid column"
        session.commit()

        for key, status in updated_attributes.items():
            print(f"{key}: {status}")
        
        print("User data updated successfully.")
    else:
        print("User not found.")



def update_user_data(user_id: int, **kwargs):
    ''' update the database and returns the information fo the new value on user_id'''
    user = session.query(User).filter(User.user_id_ == user_id).first()
    if user:
        updated_attributes = {}
        for key, value in kwargs.items():
            if hasattr(User, key):
                setattr(user, key, value)
                updated_attributes[key] = f"Updated Value is {value}"
            else:
                updated_attributes[key] = "Ignored - Not a valid column"
        session.commit()
        
        updated_info = "\n".join([f"{key}: {status}" for key, status in updated_attributes.items()])
        result_message = f"User ID {user_id} attributes update result:\n{updated_info}"
        return result_message
        
    else:
        return "User not found."



def get_all_users():
    '''Get all users from the database'''
    users = session.query(User).all()
    session.close()
    return users


def count_total_users():
    '''Count the total number of users'''
    count = session.query(User).count()
    session.close()
    return count








def main():

    # print("Starting the Works")
    create_tables()
    users = get_all_users()
    for user in users:
        print(user.user_name_, user.token_)
    print(count_total_users())
    print(update_user_data(222))
    # add_user_and_return_id(121, "ranaa", "Ra Na ", datetime.now(), "a", 1234, datetime(2022, 12, 31))

    # print(type(get_user_by_id(1)))
    # print(get_user_by_id(1))
    # print("Token count is", get_user_by_id(1).token_)
    # print("validity date is",get_user_by_id(1).valid_until_)
    # session = get_session()

    # user1 = User(12, "rana", "Ra Na", datetime.now(), "a")
    # session.add(user1)
    # session.commit()
    # print("Works End Successfully ")


if __name__ == "__main__":
    main()
