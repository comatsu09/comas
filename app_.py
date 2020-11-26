from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///user.db')
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, unique=True)
    email = Column(String)
    name = Column(String)

    def __repr__(self):
        return "User<{}, {}, {}>".format(self.id, self.email, self.name)

Base.metadate.create_all(engine)
SessionMaker = sessionmaker(bind=engine)
session = SessionMaker()

user1 = User(email="thisisme@test.com", name="Python")
session.add(user1)
session.commit()
