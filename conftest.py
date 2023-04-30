import pytest


@pytest.fixture()
def make_user():
    def make_user(name, email, password):
        return {"name": name, "email": email, "password": password}
    return make_user


@pytest.fixture()
def correct_user(make_user):
    return make_user(name='Евгений', email='evgeniy7555@yandex.ru', password='MicHail873')


@pytest.fixture()
def incorrect_password_user(make_user):
    return make_user(name='Яся', email='yasya9654@yandex.ru', password='pass')


@pytest.fixture()
def incorrect_email_user(make_user):
    return make_user(name='Яся', email='yasya9654', password='MyPass88')