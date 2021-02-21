import os
from unittest.case import TestCase

from starlette import status
from starlette.testclient import TestClient

from db.connection import SessionLocal, Base, engine
from db.models import Student
from main import app


class TestStudents(TestCase):

    def setUp(self) -> None:
        self.client = TestClient(app=app)
        Base.metadata.create_all(bind=engine)

    def tearDown(self) -> None:
        Base.metadata.drop_all(bind=engine)

    @classmethod
    def tearDownClass(cls) -> None:
        os.remove('sql_app.db')

    def test_list_students(self):
        session = SessionLocal()
        session.add_all([Student(name=f'fake name {i}', email=f'fake email {i}') for i in range(10)])
        session.commit()

        response = self.client.get('/students/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertIsInstance(response.json(), list)
        self.assertEqual(len(response.json()), 10)

    def test_create_students(self):
        student = {
            'name': 'juan',
            'email': 'email@example.com'
        }
        response = self.client.post('/students/', json=student)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        student_response = response.json()
        self.assertEqual(student_response['name'], student['name'])
        self.assertEqual(student_response['email'], student['email'])
