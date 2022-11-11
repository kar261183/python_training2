from Contacts.fixture_cont.application_cont import Application
from Contacts.model_cont.cont import Cont
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_cont(app):
    app.session_cont.login(username="admin", password="secret")
    app.cont.create(Cont(firstname="Karina", lastname="Tkachenko", mobile="8675757474", email="rfr@jjj.com"))
    app.session_cont.logout()


def test_add_empty_cont(app):
    app.session_cont.login(username="admin", password="secret")
    app.cont.create(Cont(firstname="", lastname="", mobile="", email=""))
    app.session_cont.logout()
