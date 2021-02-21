from fastapi.params import Depends

from api.models import Student, CreateStudent
from repositories.student_repository import StudentRepository


class StudentAPI:

    def list(self, student_repository: StudentRepository = Depends(StudentRepository)) -> list[Student]:
        return student_repository.list()

    def create(self, student: CreateStudent, student_repository: StudentRepository = Depends(StudentRepository)) -> Student:
        return student_repository.create(name=student.name, email=student.email)
