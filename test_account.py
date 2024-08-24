import pytest
import requests
import faker
from pprint import pprint
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


# @pytest.fixture()
# def set_url():
#     return "http://5.63.153.31:5051/v1/account"
#
#
# @pytest.fixture()
# def headers():
#     return {
#         'accept': '*/*',
#         'Content-Type': 'application/json'
#     }


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
    pprint(data)
    response = client.register_user(data)
    print()
    print(response.status_code)
    print(response.text)
