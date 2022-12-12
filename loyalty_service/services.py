import opentracing
from opentracing_instrumentation import get_current_span, span_in_context

from models import Bonus
import schemas
import uuid


async def get_all_bonuses() -> list[Bonus]:
    tracer = opentracing.global_tracer()
    with tracer.start_span(get_all_bonuses.__name__, child_of=get_current_span()) as span:
        with span_in_context(span):
            return Bonus.objects


async def create_bonus(bonus: schemas.CreateBonus) -> Bonus:
    tracer = opentracing.global_tracer()
    with tracer.start_span(create_bonus.__name__, child_of=get_current_span()) as span:
        with span_in_context(span):
            mov = Bonus(
                id=uuid.uuid4(),
                user_id=bonus.user_id,
                bonus_count=bonus.bonus_count,
            ).save()
            return mov
