# importing SQLalchemy importants 
from sqlalchemy import create_engine, String # type: ignore
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import Session
from sqlalchemy import text

# Creating an engine object to run SQLalchemy
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
'''with Session(engine) as session:
    user = User(name="Rahul")
    user = User(name='Alex')

    session.add(user)
    session.commit()

    print("User created:", user.id, user.name)'''

# selecting and printing everything from the table using text
with engine.connect() as conn:
    names = conn.execute(text("SELECT * FROM habits"))
    for i in names:
        print(i)
    print()

# selecting and printing everything from the table using session - code no 39 also does the same thing
stmt = text("SELECT * FROM habits")
with Session(engine) as session:
    result = session.execute(stmt)
    for k in result:
        print(k)

stmt1 = text("DELETE FROM habits WHERE id>1")
with Session(engine) as session:
    session.execute(stmt1)
    session.commit()