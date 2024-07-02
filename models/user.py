from config.database import Base
from sqlalchemy import Column, String

class User(Base):

    __tablename__="users"

    email = Column(String)
    password = Column(String)