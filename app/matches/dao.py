from sqlalchemy import select
from sqlalchemy.orm import selectinload, joinedload
from app.dao.base import BaseDAO
from app.matches.models import match, team
from app.database import async_session_maker

class matchDAO(BaseDAO):
    model = match

    # @classmethod
    # async def find_full_data(cls, match_id: int):        
    #     async with async_session_maker() as session:
    #         # Первый запрос для получения информации о матче
    #         # query_match = select(cls.model).filter_by(id = match_id)
    #         query_match = select(cls.model).options(
    #             joinedload(cls.model.first_team),   # Запрос первой команды
    #             joinedload(cls.model.second_team)   # Запрос второй команды
    #         ).filter_by(id=match_id)
    #         result_match = await session.execute(query_match)
    #         match_info = result_match.scalar_one_or_none()

    #         if not match_info:
    #             return None
            
    #         # Второй запрос для получения информации о командах
    #         # query_team1 = select(team).filter_by(id=match_info.first_team_id)
    #         # query_team2 = select(team).filter_by(id=match_info.second_team_id)
    #         # result_team1: team | None  = await session.execute(query_team1)
    #         # result_team2: team | None = await session.execute(query_team2)
    #         # match_data = match_info.to_dict()
    #         # match_data['first_team'] = result_team1.name
    #         # match_data['second_team'] = result_team2.name
    #         match_data = match_info.to_dict()
    #         match_data['first_team'] = match_info.first_team.name
    #         match_data['second_team'] = match_info.second_team.name
    #         return match_data


    # @classmethod
    # async def find_full_data(cls, match_id: int):
    #     async with async_session_maker() as session:
    #         query = select(cls.model).options(joinedload(cls.model.team)).filter_by(id=match_id)
    #         result = await session.execute(query)
    #         match_info = result.scalar_one_or_none()

    #         # Если матч не найден возвращаем None
    #         if not match_info:
    #             return None
            
    #         match_data = match_info.to_dict()
    #         match_data['team1'] = match_info.team.name
    #         return match_data