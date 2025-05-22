from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id:int
    username:str
    email:str

users = [
    User(
        id = 134234,
        username = "adgitl",
        email = "adgitl@gmail.com"
    ),
]

@app.get("/users")
def index():
    return users

@app.get("/users/{user_id}")
def index(user_id:int):
    for i in list:
        if i["id"] == user_id:
            return i

@app.post("/create_user")
def index(new_user: User):
    users.append(new_user)
    return new_user