from fastapi import APIRouter, status, HTTPException
from schemas import CreateBonus, Bonus, UpdateBonus
import services
import mappers


router = APIRouter(
    tags=['Loyalty'],
    prefix='/loyalty',
)


@router.get('/', status_code=status.HTTP_200_OK, response_model=list[Bonus])
async def get_bonuses():
    bonuses = await services.get_all_bonuses()
    output = [
        mappers.mapping_model_schema(bonus)
        for bonus in bonuses
    ]
    return output


@router.post('/add', status_code=status.HTTP_201_CREATED, response_model=Bonus)
async def add_bonus(bonus: CreateBonus):
    bon = await services.create_bonus(bonus)
    return mappers.mapping_model_schema(bon)


@router.delete('/{user_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_bonus(user_id: int):
    raise HTTPException(
        status_code=404,
        detail=f"Not Found a user with id {user_id}",
    )
