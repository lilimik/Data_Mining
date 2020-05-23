import vk_api

vk_session = vk_api.VkApi('+79196333094', '081011235813MiXaIlLiLiMik0180')
vk_session.auth()

vk = vk_session.get_api()
my_id = 'lilimikim'


def get_groups(friends_id):
    return vk_session.method('groups.get', {
        'user_id': friends_id, 'extended': 1, 'fields': 'activity'
    })


def my_groups_subjects(my_id):
    my_groups = []


groups = get_groups(my_id).get('items')
for group in groups:
    try:
        if group['activity'] != 'Открытая группа' and group['activity'] != 'Закрытая группа' \
                and group['activity'] != 'Частная группа' and group['activity']:
            my_groups.append(group['activity'])
            except KeyError:
        continue
    return my_groups


def get_friends():
    return vk_session.method('friends.get', {
        'user_id': my_id, 'fields': 'first_name'
    })


def get_friends_id():
    return vk_session.method('friends.get', {
        'user_id': my_id
    })


friends = get_friends().get('items')
my_groups = my_groups_subjects(my_id)


def countGroups():
    i = 0


for friend in friends:
    friends_id = friend.get('id')
    if friend.get('deactivated') is None:
         groups = get_groups(friends_id).get('items')
    for group in groups:
        try:
         for my_group in my_groups:
            if group['activity'] == my_group:
            i += 1
break
except KeyError:
continue
break
else:
continue
return i

print(countGroups())
