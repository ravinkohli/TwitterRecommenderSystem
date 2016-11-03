import math
import json
from flask import Flask, jsonify

app = Flask(__name__)

with open('database.json', 'r') as fp:
    user = json.load(fp)

with open('user_database.json', 'r') as fp:
    client_user = json.load(fp)


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


def nearest_neighbour(username,k):
    distances = {}
    for key in username.keys():
        user1 = key
    for value in username.values():
        user_name = value
    for user2 in usernames:
        if user1 != user2:
            distances.update({user2: cosine_similarity(user_name,user[user2])})

    neighbour = {}
    sorted_values = sorted(distances.values(), reverse=True)
    sorted_keys = sorted(distances, key=distances.get,reverse=True)
    for i in range(0, k):
        neighbour[sorted_keys[i]] = sorted_values[i]
    return neighbour

"""
Katy perry is added for testing purposes
"""
katyperry = {"katyperry": {'parent': 0.0, ' a': 0.0, 'childrensla': 0.0, 'dropthemichrc': 0.0, 'it': 0.004555635565060778, 'berniesand': 0.0, 'bottl': 0.0, 'jaw': 0.0, 'sweet': 0.0, 'beatsbydr': 0.0, 'class': 0.0008075347907358804, 'hang': 0.0, 'life': 0.0, 'medit': 0.0, 'karlbeck': 0.0, 'the': 0.014991142163237698, 'alway': 0.0, 'cher': 0.0, 'rejectedjok': 0.0, 'paper': 0.0, ' true': 0.0, 'memori': 0.0, 'elect': 0.0, 'yo…': 0.0, 'endors': 0.0, 'loss': 0.0, 'timelin': 0.0, 'night': 0.00014636631770760552, 'your': 0.014736544595161894, 'lenadunham': 0.0, 'scott_myrick': 0.0, 'univers': 0.0, 'debat': 0.0, 'twitter': 0.0, 'birbig': 0.0, 'and': 0.017167337732630402, 'chelseahandl': 0.0, 'moscow': 0.0, 'godmoth': 0.0, 's/o': 0.0, 'nov': 0.0, 'on': 0.0021795226614015604, 'countri': 0.0, 'ilysm': 0.0, 'debatenight': 0.0, 'jonlovett': 0.0, 'anagastey': 0.0, 'therapi': 0.0, 'tonight': 0.00202359465054494, 'our': 0.0, 'scienc': 0.0, 'great': 0.004793171637686385, 'transform': 0.0, 'freakin': 0.0, 'lyric': 0.0, 'at': 0.0012369461232062766, 'si': 0.0, 'voguemagazin': 0.0, 'deba…': 0.0, 'im': 0.0, 'mic': 0.0, 'r': -0.0, 'time': 0.0001733535247976266, 'constitut': 0.0, 'are': 0.014126559444414216, 'hill': 0.0, 'bettemidl': 0.0, 'crazi': 0.0, 'screenshot': 0.0, 'babi': 0.0, 'tweet': 0.0, 'b.i.g.l.i': 0.0, 'screamkng': 0.0, 'now': 0.0038527129738429957, 'histori': 0.0, 'respect': 0.0, 'a': -0.00027595584232786174, 'jessesaintjohn': 0.0, 'all': 0.006089029784064622, 'term': 0.0, 'dont': 0.0, 'secretari': 0.0, 'fuck': 0.0, 'celebr': 0.0, 'state': 0.0, 'bijanstephen': 0.0, 'sallykohn': 0.0, 'nasti': 0.0, 'dinner': 0.0015004857156053527, 'tvmcgee': 0.0, 'into': 0.0018701642119039903, 'number': 0.001228045382930158, 'divers': 0.0, 'becker': 0.0, 'you': 0.024400515501005637, 'felt': 0.0, 'notori': 0.0, 'guess': 0.0, 'very…': 0.0, 'we': 0.0009773767806657654, 'part': 0.0, 'parti': 0.0, 'run': 0.0, 'puppet': 0.0, 'ballot': 0.0, 'poll': 0.0, 'tabl': 0.0, 'pleas': 0.0, '⤵️': 0.0, 'iamkidpresid': 0.0, 'meme': 0.0, 'mouth': 0.0, 'come': 0.0, 'sarahksilverman': 0.0, 'with': 0.009002914293632118, 'mate': 0.0062592368086850335, 'back': 0.0, 'boss': 0.0, 'club': 0.0, 'goe': 0.0, 'to': 0.013894456966434947, 'sia': 0.0, 'cab': 0.0, 'live': 0.0, 'gif': 0.0, '❤️': 0.0, 'getglucki': 0.0, 'job': 0.0, 'typo': 0.0, 'millenni': 0.0, 'nov…': 0.0, 'amp': 0.000429002799112073, 'syria': 0.0, 'pageant': 0.0, 'even': 0.0037403284238079807, 'drum': 0.0, 'ocean': 0.0, 'happi': 0.0, 'luck': 0.0, 'woman': 0.0, 'real': 0.001347055276964403, 'hea': 0.0, 'hillaryclinton': 0.0, 'debatenight…': 0.0, 'seat': 0.0, 'minut…': 0.0, 'imwithh': 0.0, 'right': 0.005610492635711971, 'malbec': 0.0, 'bill': 0.0008075347907358804, 'karl': 0.0, 'everybodi': 0.0, 'watch': 0.00031884640040299756, ' instant messag': 0.0, 'word': 0.0005021912212578374, 'ftw': 0.0, 'dissect': 0.0, 'man': 0.0, 'putin': 0.0014182720196974816, 'wi…': 0.0, 'uncomfo': 0.0, 'everyth': 0.0, 'ones❗️': 0.0, 'suprem': 0.0, 'senat': 0.0, 'util': 0.0, 'petal': 0.0, 'rapper': 0.0, 'shellback': 0.0, 'tt': 0.0, 'martin': 0.0, 'miss': 0.0, 'grave': 0.0, 'scorpio': 0.0, 'marchesafashion': 0.0, 'person': 0.0016150695814717607, 'rule': 0.0, 'ok': 0.0, 'yougotthi': 0.0, 'cover': 0.0, 'pepperoni': 0.0, 'queen': 0.0, 'sourc': 0.0, 'studio': 0.0, 'thank': 0.0, 'polici': 0.0, 'up': 0.0012842376579476652, 'offic': 0.0, 'realdonaldtrump': 0.001228045382930158, 'tub': 0.0, 'choker': 0.0, 'trump': 0.02996443676668163, 'covergirl': 0.0, 'get': 0.0031954477584575903, 'chess': 0.0, 'badhombr': 0.0, 'madam': 0.0, 'ronanfarrow': 0.0, 'jackgarratt': 0.0, 'liiif': 0.0, '*teeth': 0.0, 'unproud': 0.0, 'post': 0.0, 'my': 0.003711875153817103, 'care': 0.0, 'tag': 0.0, 'ya': 0.0, 'cycl': 0.0, 'girl': 0.0, 'quot': 0.0, 'donald': 0.012803828263086386, 'tracksuit': 0.0, 'hillari': 0.0, 'women': 0.01674483190617771, 'oct': 0.0, 'presid': 0.0, 'nobodi': 0.0, 'have': 0.015004857156053528, 'frank': 0.0, 'fairi': 0.0, 'someon': 0.0, ' repli': 0.0, '“two': 0.0, 'bes…': 0.0, 'acknowledg': 0.0, 'season': 0.0, 'guy': 0.0, 'white': 0.0, 'señorita': 0.0, 'lot': 0.0004886883903328827, 'shoot': 0.0, 'cosbi': 0.0, 'yungskeet': 0.0, 'more': 0.001347055276964403, 'lift': 0.0, 'democraci': 0.0, 'yaaaaaasssssssssss': 0.0, 'world': 0.0005448806653503901, 'novemb': 0.0, 'bravo': 0.0, 'sleep': 0.0, 'debat…': 0.0, 'court': 0.0, 'brain': 0.0, '✨': 0.0, 'art': 0.0, 'shannonwoodward': 0.0, 'pleasur': 0.0, 'peopl': 0.0, 'steel': 0.0, 'chanc': 0.0, 'herstori': 0.0, 'drop': 0.0, 'bihday': 0.0, 'smile': 0.0, 'angel': 0.0, 'ameliashowalt': 0.0, 'ad': -0.0, 'decis': 0.0, 'jefferson': 0.0, 'again❗️cc': 0.0, 'make': 0.001215396568734256, 'katyperri': 0.0, ' know': 0.0, 'dream': 0.0, '-donald': 0.0, 'issu': 0.0, 'penc': 0.0, 'america': 0.007262196221876154, 'l': -0.0, 'iamrashidajon': 0.0, 'way': 0.0014182720196974816, 'max': 0.0, 'thi': 0.0, 'health': 0.0, 'tv': 0.001798780538091332, 'scottsimonswvla': 0.0, ' dude': 0.0, 'room': 0.0, 'lol': 0.0, 'tommi': 0.0, 'audienc': 0.0, 'side': 0.0, 'hous': 0.0}}

client_neighbour = nearest_neighbour(client_user,5)

@app.route('/TwitterRecommenderSystem/api/v1.0/recc', methods=['GET'])
def get_tasks():
    return jsonify({'tags': client_neighbour})

if __name__ == '__main__':
    app.run(debug=True)

