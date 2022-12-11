from fastapi import APIRouter, status, HTTPException
from schemas import CreateBonus, Bonus, UpdateBonus
from utils import generate_bonuses


router = APIRouter(
    tags=['Loyalty'],
    prefix='/loyalty',
)

serial = 5
bonuses = generate_bonuses(serial)


@router.get('/', status_code=status.HTTP_200_OK, response_model=list[Bonus])
async def get_bonuses():
    return bonuses


@router.post('/add', status_code=status.HTTP_201_CREATED, response_model=Bonus)
async def add_bonus(bonus: CreateBonus):
    global serial
    new_bonus = Bonus(
        id=serial,
        user_id=bonus.user_id,
        bonus_count=bonus.bonus_count,
    )
    serial += 1
    bonuses.append(new_bonus)
    return new_bonus


@router.delete('/{user_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_bonus(user_id: int):
    for i, bonus in enumerate(bonuses):
        if bonus.user_id == user_id:
            bonuses.pop(i)
            return
    raise HTTPException(
        status_code=404,
        detail=f"Not Found a user with id {user_id}",
    )
