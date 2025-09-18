from sqlalchemy.future import select
from app.database import async_session_maker


class BaseDAO:
    model = None

    @classmethod
    async def find_all(cls, **filter_by) -> list:
        async with async_session_maker() as session:            # Создание аинхронной сессии для работы с БД
            query = select(cls.model).filter_by(**filter_by)    # Описываем необходимый запрос, который хотим выполнить (ORM)
            result = await session.execute(query)               # Подаем команду, чтобы наш запрос выполнился на сервере БД
            return result.scalars().all()                       # Все строки результата запроса извлекаются и объединяются в список
        
    @classmethod
    async def find_one_or_none_by_id(cls, data_id: int):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(id = data_id)
            result = await session.execute(query)
            return result.scalar_one_or_none()
        
    @classmethod
    async def find_one_or_none(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalar_one_or_none()
