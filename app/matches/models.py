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

    first_team: Mapped["team"] = relationship("team", foreign_keys=[first_team_id], back_populates="matches_as_first")
    second_team: Mapped["team"] = relationship("team", foreign_keys=[second_team_id], back_populates="matches_as_second")

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
    
    def to_dict(self):
        return {
            'id': self.id,
            'first_team_id': self.first_team_id,
            'second_team_id': self.second_team_id,
            'time_match': self.time_match,
            'result_first': self.result_first,
            'result_second': self.result_second
        }


# Создаем модель отношения "команда"
class team(Base):
    id: Mapped[int_pk]
    name: Mapped[team_name]
    from_country: Mapped[str]
    compound_id: Mapped[int] = mapped_column(ForeignKey("compounds.id"), nullable=False)

    # trophies: Mapped[list["trophy"]] = relationship("trophy", back_populates='teams')
    # compound: Mapped["compound"] = relationship("compound", back_populates="teams")

    matches_as_first: Mapped[list["match"]] = relationship(
        "match",
        back_populates="first_team",
        foreign_keys="[match.first_team_id]"
    )

    matches_as_second: Mapped[list["match"]] = relationship(
        "match",
        back_populates="second_team",
        foreign_keys="[match.second_team_id]"
    )

    trophies: Mapped[list["trophy"]] = relationship(
        "trophy",
        back_populates="team",
        # foreign_keys="[trophy.team_id]"
    )

    compound: Mapped["compound"] = relationship(
        "compound",
        back_populates="team",
        uselist=False
    )

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

    player1: Mapped["player"] = relationship("player", foreign_keys=[player_1], back_populates="compounds_as_player1")
    player2: Mapped["player"] = relationship("player", foreign_keys=[player_2], back_populates="compounds_as_player2")
    player3: Mapped["player"] = relationship("player", foreign_keys=[player_3], back_populates="compounds_as_player3")
    player4: Mapped["player"] = relationship("player", foreign_keys=[player_4], back_populates="compounds_as_player4")
    player5: Mapped["player"] = relationship("player", foreign_keys=[player_5], back_populates="compounds_as_player5")
    reserve_player: Mapped["player"] = relationship("player", foreign_keys=[reserve], back_populates="compounds_as_reserve")

    trainer_obj: Mapped["trainer"] = relationship("trainer", foreign_keys=[trainer], back_populates="compounds")

    team:Mapped["team"] = relationship(
        "team", 
        primaryjoin="team.compound_id==compound.id", 
        back_populates="compound",
        uselist=False
        )

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

    compounds_as_player1: Mapped[list["compound"]] = relationship(
        "compound",
        foreign_keys="compound.player_1",
        back_populates="player1"
    )
    compounds_as_player2: Mapped[list["compound"]] = relationship(
        "compound",
        foreign_keys="compound.player_2",
        back_populates="player2"
    )   
    compounds_as_player3: Mapped[list["compound"]] = relationship(
        "compound",
        foreign_keys="compound.player_3",
        back_populates="player3"
    )
    compounds_as_player4: Mapped[list["compound"]] = relationship(
        "compound",
        foreign_keys="compound.player_4",
        back_populates="player4"
    )
    compounds_as_player5: Mapped[list["compound"]] = relationship(
        "compound",
        foreign_keys="compound.player_5",
        back_populates="player5"
    )
    compounds_as_reserve: Mapped[list["compound"]] = relationship(
        "compound",
        foreign_keys="compound.reserve",
        back_populates="reserve_player"
    )

# Создаем модель отношения "тренер"
# Пока что лень что-то добавлять тренеру уникального...
class trainer(Base):
    id: Mapped[int_pk]
    first_name: Mapped[str]
    second_name: Mapped[str]
    contacts: Mapped[str]

    compounds: Mapped[list["compound"]] = relationship(
        "compound",
        foreign_keys="compound.trainer",
        back_populates="trainer_obj"
    )

class trophy(Base):
    __tablename__ = 'trophies'

    id: Mapped[int_pk]
    name: Mapped[str]
    date: Mapped[date]
    team_id: Mapped[int] = mapped_column(ForeignKey("teams.id"), nullable=False)
    
    team: Mapped["team"] = relationship("team", back_populates="trophies")