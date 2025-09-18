from sqlalchemy import ForeignKey, text, Text
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.database import Base, int_pk, team_name
from datetime import date


# Создаем модель отношения "матч"
class match(Base):
    __tablename__ = "matches"
    id: Mapped[int_pk]
    first_team_id: Mapped[int] = mapped_column(ForeignKey("teams.id"), nullable=False)  # 's' в конце, так как в БД на сервере назавние
    second_team_id: Mapped[int] = mapped_column(ForeignKey("teams.id"), nullable=False) # будет уже отредактированное
    time_match: Mapped[date]
    # result: Mapped[tuple[int, int]]   # Оказывается tuple нельзя передавать в качестве типа данных для столбца, нужно делить на 2 столбца
    result_first: Mapped[int] = mapped_column(nullable=False)
    result_second: Mapped[int] = mapped_column(nullable=False)

    team: Mapped["team"] = relationship("team", back_populates="matches")

    @property
    def result(self) -> tuple[int, int]:
        return self.result_first, self.result_second

    def __str__(self):
        return(f"{self.__class__.__name__}(id={self.id},"
               f"first_team={self.first_team_id!r},"
               f"second_team={self.second_team_id!r},"
               f"time={self.time_match})")
    
    def __repr__(self):
        return str(self)


# Создаем модель отношения "команда"
class team(Base):
    id: Mapped[int_pk]
    name: Mapped[team_name]
    from_country: Mapped[str]
    compound_id: Mapped[int] = mapped_column(ForeignKey("compounds.id"), nullable=False)

    trophies: Mapped[list["trophy"]] = relationship("trophy", back_populates='teams')
    compound: Mapped["compound"] = relationship("compound", back_populates="teams")

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, name={self.name!r})"
    
    def __repr__(self):
        return str(self)

# Создаем модель отношения "состав"
class compound(Base):
    id: Mapped[int_pk]
    player_1: Mapped[int] = mapped_column(ForeignKey("players.id"), nullable=False)
    player_2: Mapped[int] = mapped_column(ForeignKey("players.id"), nullable=False)
    player_3: Mapped[int] = mapped_column(ForeignKey("players.id"), nullable=False)
    player_4: Mapped[int] = mapped_column(ForeignKey("players.id"), nullable=False)
    player_5: Mapped[int] = mapped_column(ForeignKey("players.id"), nullable=False)
    reserve: Mapped[int] = mapped_column(ForeignKey("players.id"), nullable=False)
    trainer: Mapped[int] = mapped_column(ForeignKey("trainers.id"), nullable=False)

    def __str__(self):
        return(f"{self.__class__.__name__}(id={self.id},"
               f"player_1={self.player_1!r},"
               f"player_2={self.player_2!r},"
               f"player_3={self.player_3!r},"
               f"player_4={self.player_4!r},"
               f"player_5={self.player_5!r},"
               f"reserve={self.reserve!r},"
               f"trainer={self.trainer})")
    
    def __repr__(self):
        return str(self)

# Создаем модель отношения "игрок"
class player(Base):
    id: Mapped[int_pk]
    first_name: Mapped[str]
    second_name: Mapped[str]
    contacts: Mapped[str]

# Создаем модель отношения "тренер"
# Пока что лень что-то добавлять тренеру уникального...
class trainer(Base):
    id: Mapped[int_pk]
    first_name: Mapped[str]
    second_name: Mapped[str]
    contacts: Mapped[str]

class trophy(Base):
    __tablename__ = 'trophies'

    id: Mapped[int_pk]
    name: Mapped[str]
    date: Mapped[date]
    team_id: Mapped[int] = mapped_column(ForeignKey("teams.id"), nullable=False)
    
    team: Mapped["team"] = relationship("team", back_populates="trophies")