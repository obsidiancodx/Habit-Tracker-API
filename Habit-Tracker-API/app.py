
from fastapi import FastAPI
from sqlalchemy import select
from sqlalchemy.orm import Session

from database import engine
from models import User

app = FastAPI(title="Habit Tracker API")


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/")
def welcome_user():
    return "Welcome here! Ready to track your Habits"


@app.get("/habits")
def get_habits():
    with Session(engine) as session:
        users = session.scalars(select(User)).all()

        return [
            {
                "id": user.id,
                "name": user.name,
                "habits": user.habits
            }
            for user in users
        ]
