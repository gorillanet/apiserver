from fastapi import FastAPI
from models.UserModel import UserModel as User 

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

# Get User
@app.get("/users/{user_id}")
def get_user(user_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

# Update User
@app.put("/users/{user_id}")
def update_user(item_id: int, user: User):
    return {"item_name": user.name, "item_id": item_id}

# Create User
@app.post("/users/")
def create_user(u: User):
    return u.dict()