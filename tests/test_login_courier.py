from constants import NO_FIELD_TO_LOGIN_BODY, ACCOUNT_NOT_FOUND_BODY
from courier_utils import success_authorization_courier, authorization_courier_required_field_login, \
    authorization_courier_required_field_password, authorization_courier_incorrect_login, \
    authorization_courier_incorrect_password, authorization_non_existent_user


class TestApiLoginCourier:

    def test_success_authorization(self):
        response = success_authorization_courier(self)
        assert response.status_code == 200 and 'id' in response.json()

    def test_authorization_required_field_login(self):
        response = authorization_courier_required_field_login(self)
        assert response.status_code == 400 and response.json() == NO_FIELD_TO_LOGIN_BODY

    def test_authorization_required_field_password(self):
        response = authorization_courier_required_field_password(self)
        assert response.status_code == 400 and response.json() == NO_FIELD_TO_LOGIN_BODY

    def test_authorization_incorrect_login(self):
        response = authorization_courier_incorrect_login(self)
        assert response.status_code == 404 and response.json() == ACCOUNT_NOT_FOUND_BODY

    def test_authorization_incorrect_password(self):
        response = authorization_courier_incorrect_password(self)
        assert response.status_code == 404 and response.json() == ACCOUNT_NOT_FOUND_BODY

    def test_authorization_non_existent_user(self):
        response = authorization_non_existent_user(self)
        assert response.status_code == 404 and response.json() == ACCOUNT_NOT_FOUND_BODY

