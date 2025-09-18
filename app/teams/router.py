from fastapi import APIRouter
from app.teams.dao import TeamDAO
from app.teams.schemas import Schema_teams_add, Schema_teams_Update

router = APIRouter(prefix='/teams', tags=['Работа с командами'])


@router.post("/add/")
async def register_team(team: Schema_teams_add) -> dict:
    check = await TeamDAO.add(**team.model_dump())
    if check:
        return {'message': 'Команда успешно добавлена!', 'team': team}
    else:
        return {'message': 'Ошибка при добавлении команды!'}


@router.put("/update/")
async def update_team(team: Schema_teams_Update) -> dict:
    check = await TeamDAO.update(filter_by={'name': team.name}, from_country=team.from_country ,compound_id=team.compound_id)
    if check:
        return {'message': 'Данные команды изменены!', 'team': team}
    else:
        return {'message': 'Ошибка при обновлении команды!'}
    
@router.delete("/delete/{team_id}")
async def delete_team(team_id: int) -> dict:
    check = await TeamDAO.delete(id=team_id)
    if check:
        return {'message': f'Команда с ID {team_id} удалена!'}
    else:
        return {'message': 'Ошибка при удалении команды!'}