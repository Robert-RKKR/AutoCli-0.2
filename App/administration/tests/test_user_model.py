# Django Import:
from django.contrib.auth.hashers import check_password

# Application Import:
from django.contrib.auth.models import User

# Pytest Import:
import pytest


def test_user_model(user):
    count = User.objects.all().count()
    assert count == 1


def test_check_password(create_user):
    user = create_user()
    password = '!Cisco123'
    user.set_password(password)

    assert user.check_password(password) is True
