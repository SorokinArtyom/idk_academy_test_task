from datetime import datetime
from typing import Annotated

from sqlalchemy import func
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, declared_attr, Mapped, mapped_column
from app.config import get_db_url

# import os
# import dotenv
# dotenv.load_dotenv()

# DB_HOST = 'localhost'
# DB_PORT = '5433'
# DB_NAME = 'fast_api'
# DB_USER = os.getenv("DB_USER")
# DB_PASSWORD = os.getenv("DB_PASSWORD")

# Создание ссылки на базу данных
DATABASE_URL = get_db_url()
# DATABASE_URL = f'postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

engine = create_async_engine(DATABASE_URL)  # Создание асинхронного подключения к базе данных PostgreSQL
# Создание паттерна фабрики асинхронных сессий
# Эти сессии затем используются для вполнения транзакций в БД
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

# Настройка аннотаций для дальнейшего использования в столбцах моделей
int_pk = Annotated[int, mapped_column(primary_key=True, autoincrement=True)]
team_name = Annotated[str, mapped_column(unique=True, nullable=False)]
created_at = Annotated[datetime, mapped_column(server_default=func.now())]
updated_at = Annotated[datetime, mapped_column(server_default=func.now(), onupdate=datetime.now)]

class Base(AsyncAttrs, DeclarativeBase):    # Абстрактный класс (Не напрямую от ABC)
    """
        От данного класса наследуются все модели в приложении. Он используется для миграция и
        держит в себе информацию обо всех моделях. Нужен для Alebic для создания миграций и синхронизации
        таблиц в БД и моделей в приложении по ORM
    """
    __abstract__ = True

    @declared_attr.directive    # Определяет имя таблицы в БД на основе модели в приложении
                                # Преобразует в нижний регистр и добавляет "s" в конце строки
                                # По аналогии с подходом ORM в Django
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"
    
    # Добавим 2 столбца, которые будут хранить информацию по каждому кортежу в каждом отношении (Т.к. это базовый класс для моделей
    # от который будут наследоваться все модели ORM). Будем добавлять атрибуты времени создания кортежа и атрибут времени его модификации
    created_at: Mapped[created_at]  # Время будет устанавливаться согласно внутреннему времени сервера размещения БД, 
    updated_at: Mapped[updated_at]  # благодаря возможностям SQLalchemy