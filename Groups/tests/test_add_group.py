from Groups.model.group import Group


def test_add_group(app):
    app.group.create(Group(name="12345", header="rrrrrr", footer="l;okljkhkh"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
