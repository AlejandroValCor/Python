from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.main import app
from app import schemas
from app.config import settings
from app.database import get_db
from app.database import Base

# Testing database
# SQLAlchemy_database_url = "postgresql://postgres:password123@localhost:5432/Fast API Social Media - Test" In case there is no problem for hard coding test database.
SQLAlchemy_database_url = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name} - Test"

engine = create_engine(SQLAlchemy_database_url)

testingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    db = testingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def test_root():
    response = client.get("/")

    print(response.json().get('message'))
    assert response.json().get('message') == "Happy Corgi!!! <3 Guau Guau!"
    assert response.status_code == 200

def test_create_user():
    response = client.post("/users/", json=
        {
            "email": "corgi@dog.com",
            "password": "HappyCorgi" 
        })
    
    new_user = schemas.UserOut(**response.json())

    assert new_user.email == "corgi@dog.com"
    assert response.status_code == 201