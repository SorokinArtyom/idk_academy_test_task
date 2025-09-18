from fastapi import APIRouter
from sqlalchemy import select
from app.database import async_session_maker
from app.matches.models import match

router = APIRouter(prefix='/matches', tags=['Работа с матчами'])

@router.get("/", summary="Получить все матчи")
async def get_all_matches():
    async with async_session_maker() as session:    # Создание аинхронной сессии для работы с БД
        query = select(match)                       # Описываем необходимый запрос, который хотим выполнить (ORM)
        result = await session.execute(query)       # Подаем команду, чтобы наш запрос выполнился на сервере БД
        matches = result.scalars().all()            # Все строки результата запроса извлекаются и объединяются в список
        return matches                              # Вернется в виде JSON-ответа, так как FastAPI завернет в него список
    

