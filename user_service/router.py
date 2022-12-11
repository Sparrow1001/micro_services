from fastapi import APIRouter, status, HTTPException
from schemas import User, CreateUser
from utils import generate_users


router = APIRouter(
    tags=['Users'],
    prefix='/users',
)

serial = 5
users = generate_users(serial)


@router.get('/', status_code=200, response_model=list[User])
async def get_all_users():
    return users


@router.post('/add', status_code=201, response_model=User)
async def add_new_user(user: CreateUser):
    global serial
    new_user = User(
        id=serial,
        user_id=user.user_id,
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email
    )
    serial += 1
    users.append(new_user)
    return new_user

