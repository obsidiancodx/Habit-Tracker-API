
from fastapi import FastAPI, Depends, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from database import engine, get_db
from models import User, Habits
from schemas import HabitCreate, HabitResponse

app = FastAPI(title="Habit Tracker API")


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/")
def welcome_user():
    return "Welcome here! Ready to track your Habits"


@app.get(
        "/habits",
        response_model=list[HabitResponse],
        status_code=status.HTTP_200_OK
)
def get_habits(
    db: Session = Depends(get_db)
):
    result = db.scalars(select(Habits)).all()
    return result


@app.post(
    "/habits",
    response_model=HabitResponse,
    status_code=status.HTTP_201_CREATED
)
def create_habit(
    habit_data: HabitCreate,
    db: Session = Depends(get_db)
):
    new_habit = Habits(**habit_data.model_dump())

    db.add(new_habit)
    db.commit()
    db.refresh(new_habit)

    return new_habit
