import allure
import jsonschema

from litres_project.schema.load_schema import load_schema
from litres_project.utils.api_requests import api_get


@allure.epic('API. Search')
@allure.label("owner", "Devianochka")
@allure.feature("Checking the book search on the main page")
@allure.label('microservice', 'API')
@allure.tag('regress', 'api', 'normal')
@allure.severity('normal')
@allure.label('layer', 'api')
def test_successful_searching_of_book_by_title():
    schema = load_schema('searching_book.json')

    book_title = 'Стоя под радугой'
    art_types = 'text_book'
    types = 'text_book'
    url = f'/search'
    params = {"q": book_title, "art_types": art_types, "types": types}
    result = api_get(url, params=params)

    assert result.status_code == 200
    assert result.json()['payload']['data'][0]['type'] == "text_book"


@allure.epic('API. Search')
@allure.label("owner", "Devianochka")
@allure.feature("Checking the book search on the main page")
@allure.label('microservice', 'API')
@allure.label('microservice', 'Search')
@allure.tag('regress', 'api', 'normal')
@allure.severity('normal')
@allure.label('layer', 'api')
def test_unsuccessful_searching_of_book_by_title():
    schema = load_schema('failed_book_search.json')

    book_title = 'nbmcgfhmghm'
    types = 'text_book'
    url = f'/search'
    params = {"q": book_title, "types": types}
    result = api_get(url, params=params)

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert len(result.json()['payload']['data']) == 0
