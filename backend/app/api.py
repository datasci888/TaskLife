import os
from fastapi_sqlalchemy import DBSessionMiddleware, db
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import User as ModelUser
from schemas import User as SchemaUser
from dotenv import load_dotenv

load_dotenv('.env')
DATABASE_URL = os.getenv('DATABASE_URL')

app = FastAPI()

origins = [
    "*"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URL'])


@app.post("/api/signup", response_model=SchemaUser)
async def signUp(user: SchemaUser):
    user = request_data.get("username")
    email = request_data.get("email")
    request_data = request_data.get("password")

    db_user = ModelUser(username=user.username, email=user.email, password=user.password)
    db.session.add(db_user)
    db.session.commit()
    return {"message": user}

@app.post("/api/login")
async def singUp(request_data: dict):
    user = request_data.get("username")
    return {"message": user}
