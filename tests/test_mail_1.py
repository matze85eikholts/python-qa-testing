import pytest


@pytest.fixture()
def set_up():
    print("Log in was executed")


#  email can be sent only after successful login therefore the fixture should be used
def test_sending_mail_1(set_up):
    print("Email_1 has been sent")


def test_sending_mail_2(set_up):
    print("Email_2 has been sent")
