import allure
import jsonschema
from litres_project.schema.load_schema import load_schema
from litres_project.utils.api_requests import api_post
from tests.api.conftest import email, password, invalid_password


@allure.epic('API. Authorized')
@allure.label("owner", "Devianochka")
@allure.feature("Checking the authorization of the user")
@allure.label('microservice', 'API')
@allure.tag('regress', 'api', 'normal')
@allure.label('layer', 'api')
@allure.severity('normal')
def test_authorization_registered_user():
    schema = load_schema('authorization.json')
    url = "/auth/login"

    result = api_post(url, json={"login": email, "password": password})

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert result.json()['error'] is None


@allure.epic('API. Authorized')
@allure.label("owner", "Devianochka")
@allure.feature("Checking the authorization of the user")
@allure.label('microservice', 'API')
@allure.tag('regress', 'api', 'normal')
@allure.label('layer', 'api')
@allure.severity('normal')
def test_authorization_unregistered_user():
    schema = load_schema('failed_authorization.json')
    url = "/auth/login"


    result = api_post(url, json={"login": email, "password": invalid_password})

    assert result.status_code == 401
    jsonschema.validate(result.json(), schema)
    assert result.json()['error']['type'] == "Unauthorized"
    assert result.json()['error']['title'] == "Incorrect user data"
