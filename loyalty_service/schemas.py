from pydantic import BaseModel


class BaseBonus(BaseModel):
    user_id: int
    bonus_count: int


class Bonus(BaseBonus):
    id: int


class CreateBonus(BaseBonus):
    ...


class UpdateBonus(BaseBonus):
    ...

