import nltk
from nltk.corpus import stopwords
from nltk import tag


def read_tweets(file):
    data = []
    f = open(file, "r")
    for line in f:
        data.append(line)
    return data

# test_data = read_tweets("Tweets_PrePOS.txt")





def tag_pos(data):
    pos_data = []
    post_list = []
    for row in data:
        row = nltk.word_tokenize(row)
        row = nltk.pos_tag(row)
        post_list.append(row)
        pos_data.append(post_list)
        post_list = []
    pos_data = pos_data[1:]
    return pos_data

# pos_data = tag_pos(test_data)


porter = nltk.PorterStemmer()


def stemming_stop_removal(porter, data):
    sns_pos_data = []
    sns_list = []
    stop = stopwords.words('english')
    for row in data:
        for tweet in row:
            for (word, tags) in tweet:
                if word not in stop:
                    word = porter.stem(word)
                    tagged_token = tag.str2tuple(word + "/" + tags)
                    sns_list.append(tagged_token)
                else:
                    continue
            sns_pos_data.append(sns_list)
            sns_list = []
    return sns_pos_data

# sns_pos_data = stemming_stop_removal(porter, pos_data)

# print(sns_pos_data[:3])
