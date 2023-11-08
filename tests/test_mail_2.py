import pytest


@pytest.fixture()
def set_up():
    print("Login was executed")

def test_sending_mail_1():
    print("Email_1 was sent")

def test_sending_mail_2():
    print("Email_2 was sent")