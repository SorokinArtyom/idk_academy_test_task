from fastapi import APIRouter, Depends
from app.matches.dao import matchDAO
from app.matches.rb import RBMatch
from app.matches.schemas import Schema_match

router = APIRouter(prefix='/matches', tags=['Работа с матчами'])

@router.get("/", summary="Получить все матчи", response_model=list[Schema_match])
async def get_all_matches(request_body: RBMatch = Depends()) -> list[Schema_match]:
    return await matchDAO.find_all(**request_body.to_dict())    # Вернется в виде JSON-ответа, так как FastAPI завернет в него список

@router.get("/{id}", summary="Получить 1 матч по id")
async def get_match_by_id(match_id: int) -> Schema_match | None:
    result = await matchDAO.find_one_or_none_by_id(match_id)
    if result is None:
        return {'message': f'Матч с ID {match_id} не найден!'}
    return result

@router.post("/by_filter", summary="Получить матчи по фильтру")
async def get_match_by_filter(request_body: RBMatch = Depends()) -> list[Schema_match] | dict:
    result = await matchDAO.find_all(**request_body.to_dict())
    if result is None:
        return {'message': f'Матчи с указанными вами параметрами не найден!'}
    return result

# @router.get("/{id}", summary="Получить один матч по ID с дополнением данных из другой таблицы")
# async def get_match_by_id(match_id: int) -> Schema_match | dict:
#     result = await matchDAO.find_full_data(match_id=match_id)
#     if result is None:
#         return {'message': f'Матч с ID {match_id} не найден!'}
#     return result