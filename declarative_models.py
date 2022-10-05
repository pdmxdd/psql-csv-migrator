from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import BigInteger
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Users(Base):
    __tablename__ = "users"
    id = Column(BigInteger, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    auth_email = Column(String)

class Cars(Base):
    __tablename__ = "cars"
    id = Column(BigInteger, primary_key=True)
    make = Column(String)
    model = Column(String)

class CarsUsers(Base):
    __tablename__ = "cars_users"
    user_id = Column(BigInteger)
    car_id = Column(BigInteger)

    __mapper_args__ = {
        "primary_key": [user_id, car_id]
    }

