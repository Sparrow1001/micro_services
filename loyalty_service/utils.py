import uuid
import random

from schemas import Bonus


def generate_bonuses(number) -> list[Bonus]:
    return [
        Bonus(
            id=i,
            user_id=random.randint(1, 100),
            bonus_count=random.randint(1, 10000),
        ) for i in range(number)
    ]
