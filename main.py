from sqlalchemy import create_engine, Column, Integer, String, Boolean, BigInteger, DateTime, Float
from contextlib import contextmanager
import psycopg2
from sqlalchemy.orm import declarative_base, sessionmaker

db_url = 'postgresql+psycopg2://postgres:serge2002@127.0.0.1:5432/univer'  # server
engine = create_engine(db_url, pool_size=100, max_overflow=25, pool_recycle=60, pool_pre_ping=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()


def create_all_tables():
    Base.metadata.create_all(engine)


@contextmanager
def session_scope():
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    phone_number = Column(String)
    car_number = Column(String)
    order_id = Column(Integer)
    car_marka = Column(String)
    car_model = Column(String)


create_all_tables()
