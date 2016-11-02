import math
from textblob import TextBlob as tb


def tf(word, blob):
    return blob.words.count(word) / len(blob.words)


def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob)


def idf(word, bloblist):
    return math.log(len(bloblist) / (1 + n_containing(word, bloblist)))


def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)


def tfidf_rank(data,i,user):
    bloblist = []
    user_list = {}
    for x in range(1,i+1):
        stre = str(x)
        f = open("tw_db/t" + stre + ".txt", "r")
        text = ""
        for line in f:
            text = line + " " + text
        bloblist.append(tb(text))
    for i, blob in enumerate(bloblist):
        for tweet in data[i]:
            scores = {word: tfidf(word, blob, bloblist) for word in tweet if word != ""}
        sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        user_list[user[i]] = sorted_words
    return user_list


def tfidf_rank_user(data,i,user):
    bloblist = []
    for x in range(0, i + 1):
        stre = str(x)
        f = open("tw_db/t" + stre + ".txt", "r")
        text = ""
        for line in f:
            text = line + " " + text
        bloblist.append(tb(text))
    f.close()
    for i, blob in enumerate(bloblist):
        print(type(blob))
        for tweet in data:
            scores = {word: tfidf(word, blob, bloblist) for word in tweet if word != ""}
        sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        return {user[0]: sorted_words}
