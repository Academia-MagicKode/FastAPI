from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLACHAMY_TEST_DATABASE_URL= "sqlite:///./test.db"

engine= create_engine(SQLACHAMY_TEST_DATABASE_URL,
    connect_args={"check_same_thread": False})


TestingSessionLocal= sessionmaker(bind=engine, autocommit=False, autoflush=False, )
BaseTest = declarative_base()

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()