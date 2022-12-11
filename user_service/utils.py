import uuid
import random

from schemas import User


def generate_users(number) -> list[User]:
    return [
        User(
            id=i,
            user_id=random.randint(10, 1000),
            first_name=str(uuid.uuid4()),
            last_name=str(uuid.uuid4()),
            email=random.randint(1000, 5000)
        ) for i in range(number)
    ]
