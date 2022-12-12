import mongoengine


class Bonus(mongoengine.Document):
    meta = {
        'db_alias': 'mydb',
        'collection': 'bonuses',
    }

    id = mongoengine.UUIDField(primary_key=True)
    user_id = mongoengine.IntField(required=True)
    bonus_count = mongoengine.IntField(required=True)
