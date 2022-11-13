from Groups.model.group import Group


def test_modify_group_name(app):
    app.group.modify_group(Group(name="katia"))


def test_modify_group_header(app):
    app.group.modify_group(Group(header="lollipop"))
