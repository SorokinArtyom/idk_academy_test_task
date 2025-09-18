from datetime import date
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field

class Schema_match(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    first_team_id: int = Field(..., ge=0, description="ID первой команды участвующей в матче")
    second_team_id: int = Field(..., ge=0, description="ID второй команды участвующей в матче")
    time_match: date = Field(..., description="Время начала матча")
    result_first: int = Field(..., ge=0, le=5, description="Количество очков первой команды в матче")
    result_second: int = Field(..., ge=0, le=5, description="Количество очков второй команды в матче")

    # team1: Optional[str] = Field(..., description="Название первой команды")
    # team2: Optional[str] = Field(..., description="Название второй команды")

    # team1: Optional[str] = None
    # team2: Optional[str] = None