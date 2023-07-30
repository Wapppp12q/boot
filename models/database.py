from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_NAME = 'db/users.sqlite'

Base = declarative_base()

engine = create_engine(f'sqlite:///{DATABASE_NAME}')
Session = sessionmaker(bind=engine)

Base.metadata.create_all(engine)


def create_db():
    Base.metadata.create_all(engine)