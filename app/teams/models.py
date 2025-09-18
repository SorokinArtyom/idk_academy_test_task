from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base, int_pk, team_name
# from app.matches.models import match

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
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'from_country': self.from_country,
            'compound_id': self.compound_id
        }