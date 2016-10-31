from nltk import tag

with open('Replace.txt', 'r') as document:
    Replace = {}

    for line in document:
        line = line.split(',',1)
        if not line:
            continue
        Replace[line[0]] = line[1][:-1]


with open('Dismiss.txt', 'r') as document:
    Dismiss = {}
    for line in document:
        line = line.split(',',1)
        if not line:  # empty line
            continue
        Dismiss[line[0]] = line[1][:-1]

# Two dictionaries created, Replace and Dismiss

# file = open('Tweets_PrePOS.txt','w')


def slang_removal(data,replace,dismiss):
    final_data_list = []
    user_tweets = []
    for line in data:
        for tweet in line:
            part = []
            for (word,tags) in tweet:
                if dismiss.get(word, "NO") == "NO":
                    replacement = replace.get(word, word)
                    tagged_token = tag.str2tuple(replacement + "/" + tags)
                    part.append(tagged_token)
            user_tweets.append(part)
        final_data_list.append(user_tweets)
        user_tweets = []
    return final_data_list
