class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.
    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user in group.get_users():
        return True
    for g in group.get_groups():
        if is_user_in_group(user, g):
            return True
    return False

parent = Group("parent")
parent_user = "parent_user"
parent.add_user(parent_user)

child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)


print(is_user_in_group(sub_child_user, parent))
# expected output: True
print("Pass" if is_user_in_group(sub_child_user, parent)== True else "Fail")
print('------------------------------------------')

print(is_user_in_group(sub_child_user, child))
# expected output: True
print("Pass" if is_user_in_group(sub_child_user, child)== True else "Fail")
print('------------------------------------------')

print(is_user_in_group(parent_user, parent))
# expected output: True
print("Pass" if is_user_in_group(parent_user, parent)== True else "Fail")
print('------------------------------------------')

print(is_user_in_group(parent_user, child))
# expected output: False
print("Pass" if is_user_in_group(parent_user, child)== False else "Fail")
print('------------------------------------------')

print(is_user_in_group("sub_child_user", parent))
# expected output: True
print("Pass" if is_user_in_group("sub_child_user", parent)== True else "Fail")
print('------------------------------------------')

print(is_user_in_group("super_user", parent))
# expected output: False
print("Pass" if is_user_in_group("super_user", parent)== False else "Fail")
print('------------------------------------------')


print(is_user_in_group(None, parent))
# expected output: False
print("Pass" if is_user_in_group(None, parent)== False else "Fail")
print('------------------------------------------')



empty_group = Group("emptygroup")

print(is_user_in_group(None, empty_group))
# expected output: False
print("Pass" if is_user_in_group(None, empty_group)== False else "Fail")
print('------------------------------------------')


print(is_user_in_group("User", empty_group))
# expected output: False
print("Pass" if is_user_in_group("User", empty_group)== False else "Fail")
print('------------------------------------------')