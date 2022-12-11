from pydantic import BaseModel


class BaseUser(BaseModel):
    user_id: int
    first_name: str
    last_name: str
    email: str


class User(BaseUser):
    id: int


class CreateUser(BaseUser):
    ...


class UpdateUser(BaseUser):
    ...

