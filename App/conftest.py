# Pytest Import:
import uuid
import pytest


@pytest.fixture(scope='function')
def user(db, django_user_model):
    return django_user_model.objects.create_user('test', 'test@test.pl', 'test')


@pytest.fixture(scope='function')
def test_password():
    return '!Cisco123'


@pytest.fixture(scope='function')
def create_user(db, django_user_model, test_password):
    
    def make_user(**kwargs):
        kwargs['password'] = test_password

        if 'username' not in kwargs:
            kwargs['username'] = str(uuid.uuid4())

        return django_user_model.objects.create_user(**kwargs)

    return make_user

@pytest.fixture(scope='function')
def create_users(db, django_user_model, test_password):
    
    def make_user(count=1, **kwargs):
        users = []
        kwargs['password'] = test_password

        for i in range(count):
            if 'username' not in kwargs:
                kwargs['username'] = str(uuid.uuid4())

            users.append(django_user_model.objects.create_user(**kwargs))

        return users

    return make_user
