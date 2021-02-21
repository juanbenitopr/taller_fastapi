from fastapi import APIRouter
from starlette import status

from api.endpoints import StudentAPI
from api.models import Student

router = APIRouter(prefix='/students')

student = StudentAPI()
router.add_api_route(path='/', endpoint=student.list, response_model=list[Student], status_code=status.HTTP_200_OK, methods=['GET'])
router.add_api_route(path='/', endpoint=student.create, response_model=Student, status_code=status.HTTP_201_CREATED, methods=['POST'])