from Groups.model.group import Group


def test_modify_group_name(app):
    old_groups = app.group.get_group_list()
    app.group.modify_group(Group(name="katia"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_modify_group_header(app):
    old_groups = app.group.get_group_list()
    app.group.modify_group(Group(header="lollipop"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

