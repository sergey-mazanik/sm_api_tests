import pytest
import faker
from client import Client


@pytest.fixture()
def client():
    return Client()


@pytest.fixture()
def generate_user():
    fake = faker.Faker('ru_RU')
    return {
        "login": fake.user_name(),
        "email": fake.email(),
        "password": fake.password(length=10)
    }


data = [
    # short login
    {
        "login": 'l',
        "email": 'test@test.com',
        "password": '12345678'
    },
    # invalid email
    {
        "login": 'login_12786456286912515',
        "email": 'e',
        "password": '12345678'
    },
    # short password
    {
        "login": 'login_12786456286912515',
        "email": 'test@test.com',
        "password": 'p'
    }
]


@pytest.mark.parametrize('data', data)
def test_post_v1_account(data, client):
    response = client.register_user(data)
    assert response.status_code == 400, 'Status code should be 400!'
    # assert response.status_code == 200, 'Status code should be 200!'
