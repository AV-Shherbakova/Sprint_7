from conftest import generate_random_string
from courier_utils import create_courier, create_courier_without_data, delete_courier, success_authorization_courier
from constants import USER_EXIST_BODY, NO_FIELD_TO_CREATE_BODY, USER_DATA


class TestApiCreateCourier:

    def test_success_create_courier(self):
        login = generate_random_string(8)
        password = generate_random_string(4)
        first_name = generate_random_string(8)
        response = create_courier(login, password, first_name)
        assert response.status_code == 201 and response.json() == {"ok": True}
        auth_response = success_authorization_courier(USER_DATA)
        assert auth_response.status_code == 200
        courier_id = auth_response.json().get("id")
        assert courier_id is not None
        delete_response = delete_courier(courier_id)
        assert delete_response.status_code == 200 and delete_response.json() == {"ok": True}


    def test_error_create_courier(self):
        login = generate_random_string(8)
        password = generate_random_string(4)
        first_name = generate_random_string(8)
        response = create_courier(login, password, first_name)
        assert response.status_code == 201 and response.json() == {"ok": True}

        second_response = create_courier(login, password, first_name)
        assert second_response.status_code == 409 and second_response.json() == USER_EXIST_BODY

    def test_create_required_field_login(self):
        password = generate_random_string(4)
        first_name = generate_random_string(8)
        response = create_courier_without_data(first_name, password=password)
        assert response.status_code == 400 and response.json() == NO_FIELD_TO_CREATE_BODY

    def test_create_required_field_password(self):
        login = generate_random_string(8)
        first_name = generate_random_string(8)
        response = create_courier_without_data(first_name, login=login)
        assert response.status_code == 400 and response.json() == NO_FIELD_TO_CREATE_BODY

    def test_create_required_field_first_name(self):
        login = generate_random_string(8)
        password = generate_random_string(4)
        response = create_courier_without_data(None, password=password, login=login)
        assert response.status_code == 400 and response.json() == NO_FIELD_TO_CREATE_BODY