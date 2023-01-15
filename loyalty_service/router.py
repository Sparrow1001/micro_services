import opentracing
from fastapi import APIRouter, status, HTTPException
from schemas import CreateBonus, Bonus, UpdateBonus, ApplyBonus
import services
import mappers
from opentracing_instrumentation.request_context import get_current_span, span_in_context


router = APIRouter(
    tags=['Loyalty'],
    prefix='/loyalty',
)


@router.get('/get_all_bonuses', status_code=status.HTTP_200_OK, response_model=list[Bonus])
async def get_bonuses():
    tracer = opentracing.global_tracer()
    with tracer.start_span(get_bonuses.__name__, child_of=get_current_span()) as span:
        with span_in_context(span):
            bonuses = await services.get_all_bonuses()
            output = [
                mappers.mapping_model_schema(bonus)
                for bonus in bonuses
            ]
            return output


@router.get('/get_bonus_by_id/{user_id}', status_code=status.HTTP_200_OK, response_model=Bonus)
async def get_bonus_by_id(user_id: int):
    tracer = opentracing.global_tracer()
    with tracer.start_span(get_bonus_by_id.__name__, child_of=get_current_span()) as span:
        with span_in_context(span):
            bonuses = await services.get_bonus_by_id(user_id)
            output = mappers.mapping_model_schema(bonuses)
            return output


@router.post('/add', status_code=status.HTTP_201_CREATED, response_model=Bonus)
async def add_bonus(bonus: CreateBonus):
    tracer = opentracing.global_tracer()
    with tracer.start_span(add_bonus.__name__, child_of=get_current_span()) as span:
        with span_in_context(span):
            bon = await services.create_bonus(bonus)
            return mappers.mapping_model_schema(bon)


@router.put('/apply', status_code=status.HTTP_200_OK)
async def apply_bonus(bonus: ApplyBonus):
    tracer = opentracing.global_tracer()
    with tracer.start_span(apply_bonus.__name__, child_of=get_current_span()) as span:
        with span_in_context(span):
            await services.apply_bonus(bonus)


@router.delete('/{user_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_bonus(user_id: int):
    raise HTTPException(
        status_code=404,
        detail=f"Not Found a user with id {user_id}",
    )
