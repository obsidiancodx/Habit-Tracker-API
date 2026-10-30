from fastapi import FastAPI # type: ignore

app = FastAPI(title="Habit Tracker API")

@app.get("/health")
def health_check():
    return {"status":"ok"}

@app.get("/")
def welcome_user():
    return "Welcome here (; Ready to track your Habits"