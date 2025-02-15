from fastapi.testclient import TestClient
from main import app
from database import get_db, Base, engine
from sqlalchemy.orm import sessionmaker
import pytest

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


