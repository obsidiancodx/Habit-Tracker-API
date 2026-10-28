from sqlalchemy import create_engine, String # type: ignore
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import Session

engine = create_engine("sqlite:///habits.db")
class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "Habits"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    name: Mapped[str] = mapped_column(
        String(100)
    )

    habits: Mapped[str] = mapped_column(
        String(100),
        default='No Habits Added'
    )

Base.metadata.create_all(engine)
with Session(engine) as session:
    user = User(name="Rahul")

    session.add(user)
    session.commit()

    print("User created:", user.id, user.name)
