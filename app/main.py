from fastapi import FastAPI
from app.matches.router import router as roter_matches
from app.teams.router import router as router_teams

app = FastAPI()

@app.get("/")
def home_page():
    return {"message": "Сервис для отслеживания матчей и турниров"}

app.include_router(roter_matches)
app.include_router(router_teams)