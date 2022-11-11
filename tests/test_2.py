from fixture.application import Application
from model.group import Group
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_create_group(app):
    app.login(username="admin", password="secret")
    app.create_new_group(Group(name="12345", header="rrrrrr", footer="l;okljkhkh"))
    app.logout()


def test_create_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_new_group(Group(name="", header="", footer=""))
    app.logout()