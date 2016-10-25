import nltk


def read_tweets(file):
    data = []
    f = open(file, "r")
    for line in f:
        line = line.split(" ")
        data.append(line)
    return data


test_data = read_tweets("Tweets_PrePOS.txt")
text = nltk.word_tokenize("@MailOnline If you have to do that maybe you shouldn't be trying to earn the position of the worlds most powerful person.")
"""
Use the above function for tokenising the tweets from each data
"""

print(nltk.pos_tag(text))

"""
Use the above function for POS tagging the tweets from each data
"""
