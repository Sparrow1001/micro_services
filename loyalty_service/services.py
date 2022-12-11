from models import Bonus
import schemas
import uuid


async def get_all_bonuses() -> list[Bonus]:
    return Bonus.objects


async def create_bonus(bonus: schemas.CreateBonus) -> Bonus:
    mov = Bonus(
        id=uuid.uuid4(),
        user_id=bonus.user_id,
        bonus_count=bonus.bonus_count,
    ).save()
    return mov
