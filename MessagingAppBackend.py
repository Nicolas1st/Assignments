groups = dict()
users = []


def get_existing_groups(groups):
    return groups.keys()


def group_exists(requested_group, groups):
    if requested_group in get_existing_groups():
        return True
    else:
        return False


def on_create_new_user(users, first_name, last_name):
    new_user = ([len(users), first_name, last_name])
    return users + new_user


def on_create_group(group_name, creator, groups):
    existing_groups = get_existing_groups(groups)
    if group_name not in existing_groups:
        groups[group_name] = [creator, [], []]
    return groups


def on_write_message(groups, chosen_group, author, message):
    if group_exists(chosen_group, groups):
        groups[chosen_group][2].append([author, message])
    return groups


def on_get_group_messages(group_name, groups):
    if group_exists(group_name, groups):
        return groups[group_name][2]
    else:
        return None

