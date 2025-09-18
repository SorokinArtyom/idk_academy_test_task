from pydantic import BaseModel, Field


class Schema_teams_add(BaseModel):
    id: int
    name: str = Field(..., min_length=3, max_length=50, description="Полное название команды")
    from_country: str = Field(..., max_length=50, description="Название страны, которую представляет команда")
    compound_id: int = Field(..., ge=0, le=10000, description="ID состава этой команды")

class Schema_teams_Update(BaseModel):
    name: str = Field(..., min_length=3, max_length=50, description="Полное название команды")
    from_country: str = Field(..., max_length=50, description="Название страны, которую представляет команда")
    compound_id: int = Field(..., ge=0, le=10000, description="ID состава этой команды")