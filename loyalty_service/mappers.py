import schemas
import models


def mapping_model_schema(model: models.Bonus):
    schema = schemas.Bonus(
        id=model.id,
        user_id=model.user_id,
        bonus_count=model.bonus_count,
    )
    return schema


def mapping_schema_model(schema: schemas.Bonus):
    model = schemas.Bonus(
        id=schema.id,
        user_id=schema.user_id,
        bonus_count=schema.bonus_count,
    )
    return model
