import json
import requests
from constants import URL_LOGIN_COURIER, USER_DATA, COURIER_PASSWORD, COURIER_LOGIN, NO_EXIST_USER_DATA, \
    URL_CREATE_COURIER, URL_DELETE_COURIER


def create_courier(login, password, first_name):
    courier_data = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    json_data = json.dumps(courier_data)
    headers = {"Content-Type": "application/json"}
    response = requests.post(URL_CREATE_COURIER, data=json_data, headers=headers)
    return response

def create_courier_without_data(first_name, password=None, login=None):
    courier_data = {"firstName": first_name}
    if password is not None:
        courier_data["password"] = password
    if login is not None:
        courier_data["login"] = login
    json_data = json.dumps(courier_data)
    headers = {"Content-Type": "application/json"}
    response = requests.post(URL_CREATE_COURIER, data=json_data, headers=headers)
    return response


def success_authorization_courier(self):
    json_data = json.dumps(USER_DATA)
    headers = {"Content-Type": "application/json"}
    response = requests.post(URL_LOGIN_COURIER, data=json_data, headers=headers)
    return response


def authorization_courier_required_field_login(self):
    courier_data = {
        "password": COURIER_PASSWORD
    }
    json_data = json.dumps(courier_data)
    headers = {"Content-Type": "application/json"}
    response = requests.post(URL_LOGIN_COURIER, data=json_data, headers=headers)
    return response


def authorization_courier_required_field_password(self):
    courier_data = {
        "login": COURIER_LOGIN
    }
    json_data = json.dumps(courier_data)
    headers = {"Content-Type": "application/json"}
    response = requests.post(URL_LOGIN_COURIER, data=json_data, headers=headers)
    return response

def authorization_courier_incorrect_login(self):
    courier_data = {
        "login": "Vladislaw",
        "password": COURIER_PASSWORD
    }
    json_data = json.dumps(courier_data)
    headers = {"Content-Type": "application/json"}
    response = requests.post(URL_LOGIN_COURIER, data=json_data, headers=headers)
    return response

def authorization_courier_incorrect_password(self):
    courier_data = {
        "login": COURIER_LOGIN,
        "password": "6665"
    }
    json_data = json.dumps(courier_data)
    headers = {"Content-Type": "application/json"}
    response = requests.post(URL_LOGIN_COURIER, data=json_data, headers=headers)
    return response

def authorization_non_existent_user(self):
    NO_EXIST_USER_DATA
    json_data = json.dumps(NO_EXIST_USER_DATA)
    headers = {"Content-Type": "application/json"}
    response = requests.post(URL_LOGIN_COURIER, data=json_data, headers=headers)
    return response

def delete_courier(courier_id):
    headers = {"Content-Type": "application/json"}
    response = requests.delete(f"{URL_DELETE_COURIER}{courier_id}", headers=headers)
    return response

