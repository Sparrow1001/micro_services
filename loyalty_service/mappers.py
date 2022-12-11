import opentracing
from opentracing_instrumentation import span_in_context, get_current_span

import schemas
import models


def mapping_model_schema(model: models.Bonus):
    tracer = opentracing.global_tracer()
    with tracer.start_span(mapping_model_schema.__name__, child_of=get_current_span()) as span:
        with span_in_context(span):
            schema = schemas.Bonus(
                id=model.id,
                user_id=model.user_id,
                bonus_count=model.bonus_count,
            )
            return schema


def mapping_schema_model(schema: schemas.Bonus):
    tracer = opentracing.global_tracer()
    with tracer.start_span(mapping_schema_model.__name__, child_of=get_current_span()) as span:
        with span_in_context(span):
            model = schemas.Bonus(
                id=schema.id,
                user_id=schema.user_id,
                bonus_count=schema.bonus_count,
            )
            return model
