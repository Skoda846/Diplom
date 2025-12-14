import requests
import allure

from config import BASE_URL, HEADERS


@allure.title("Поиск фильмов по 2020 году")
@allure.description("Ввод названия фильма")
@allure.severity("critical")
def test_movies_2020():

    response = requests.get(BASE_URL+"/movie?page=1&limit=10&type=movie&year=2020",
                            headers=HEADERS)
    assert response.status_code == 200


@allure.title("Поиск фильмов по ID")
@allure.description("Ввод ID")
@allure.severity("critical")
def test_by_movie_id():

    response = requests.get(BASE_URL+"/movie/1009536", headers=HEADERS)
    assert response.status_code == 200


@allure.title("Поиск фильмов")
@allure.description("Ввод названия фильма по имени")
@allure.severity("normal")
def test_by_name():

    response = requests.get(
        BASE_URL+"/movie/search?page=1&limit=10&query=%D0%9E%D1%81%D1%82%D1%80%D0%BE%D0%B2",
        headers=HEADERS)
    assert response.status_code == 200


@allure.title("Поиск актера")
@allure.description("Ввод актера")
@allure.severity("normal")
def test_by_actors():

    response = requests.get(BASE_URL+"/person/37859", headers=HEADERS)
    assert response.status_code == 200


@allure.title("Поиск рецензии")
@allure.description("Ввод рецензии")
@allure.severity("low")
def test_by_reviews():

    response = requests.get(BASE_URL+"/review?page=1&limit=10&movieId=397667", headers=HEADERS)
    assert response.status_code == 200