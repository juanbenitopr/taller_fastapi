from fastapi.params import Depends
from sqlalchemy.orm import Session

from db.connection import get_db
from db.models import Student


class StudentRepository:

    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def list(self) -> list[Student]:
        return self.db.query(Student).all()

    def create(self, name: str, email: str) -> Student:
        db_student = Student(name=name, email=email)
        self.db.add(db_student)
        self.db.commit()
        self.db.refresh(db_student)
        return db_student
