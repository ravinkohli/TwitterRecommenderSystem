import math
import json

with open('database.json', 'r') as fp:
    user = json.load(fp)

def cosine_similarity(user1,user2):
    dot_product = 0
    for key, value in user1.items():
        if key in user2.keys():
            dot_product = dot_product + float(value) * float(user2[key])
    mod_user1 = 0
    for value in user1.values():
        mod_user1 = mod_user1 + float(value) * float(value)
    mod_user1 = math.sqrt(mod_user1)
    mod_user2 = 0
    for value in user2.values():
        mod_user2 = mod_user2 + float(value) * float(value)
    mod_user2 = math.sqrt(mod_user2)
    if dot_product != 0:
        return dot_product/mod_user2 * mod_user1
    else:
        return 0

usernames = user.keys()


def nearest_neighbour(user1,k):
    distances = {}
    for user2 in usernames:
        if user1 != user2:
            distances.update({user2: cosine_similarity(user[user1],user[user2])})

    neighbour = {}
    sorted_values = sorted(distances.values(), reverse=True)
    sorted_keys = sorted(distances, key=distances.get,reverse=True)
    for i in range(0, k):
        neighbour[sorted_keys[i]] = sorted_values[i]
    return neighbour


print(nearest_neighbour("selenagomez",5))
