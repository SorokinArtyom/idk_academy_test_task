from app.dao.base import BaseDAO
from app.teams.models import team

class TeamDAO(BaseDAO):
    model = team