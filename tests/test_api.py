
import requests
from pytest_voluptuous import S
from requests import Response


from tests.schemas.schema import resource_list_schema


def test_assert_code_status():
    response: Response = requests.get(url='https://reqres.in/api/unknown')
    print(response)
    assert response.status_code


def test_assert_response():
    response: Response = requests.get(url='https://reqres.in/api/unknown/2')
    print(response.json())

    assert response.json().get('data').get('pantone_value')


def test_assert_number_of_letters():
    response: Response = requests.get('https://reqres.in/api/unknown/2')

    color = response.json().get('data').get('pantone_value')
    print(color)
    assert len(response.content) == 232


def test_schema_resource_list():
    result = requests.get(url="https://reqres.in/api/unknown", params={"page": 4})

    assert S(resource_list_schema) == result.json()


def test_number_of_page():
    response: Response = requests.get(url="https://reqres.in/api/unknown")

    page = response.json().get("per_page")

    assert page == 6


def test_register():

    result = requests.post(url="https://reqres.in/api/register", data={"email": "user123@gmail.com",
                                                                       "password": "Qwerty123"})

    print(result)
    assert result.status_code


def test_assert_data():
    response: Response = requests.get(url="https://reqres.in/api/unknown/2")

    assert response.json().get("data").get("name") == "fuchsia rose"






