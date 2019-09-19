fst_paragraph = "Jesper"

count = {}
i = 0
for c  in fst_paragraph:
    count.setdefault(c, 0)
    count[c] += i

print(count)

img = {'he': 'hej', 'google': [393952,39552,29992211]}

print(img["google"][1])


users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'locations': ['princeton', 'copenhagen'],
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'locations': ['paris', 'athens'],
    },
}

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    locations = user_info['locations']

    print("\tFull name: " + full_name.title())
    for location in locations:
        print("\tLocation: " + location.title())