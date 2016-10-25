import stopword_removal_stemming
import nltk
import re
import preprocessing
from nltk import tag

def processing(data, username):
    data = preprocessing.remove_links(data)
    data = preprocessing.remove_username("@"+ username, data)
    data = preprocessing.remove(":", data)
    data = preprocessing.remove("\n", data)
    data = preprocessing.remove("RT", data)
    emoji_pattern = re.compile("["u"\U0001F600-\U0001F64F""]+", flags=re.UNICODE)
    data = preprocessing.remove_emoji(emoji_pattern,data)
    emoji_pattern = re.compile("["u"\U0001F300-\U0001F5FF""]+", flags=re.UNICODE)
    data = preprocessing.remove_emoji(emoji_pattern,data)
    return data


def pos_tag():
    test_data = []
    test_data_list = []
    for x in range(1, 100):
        stre = str(x)
        test_data = stopword_removal_stemming.read_tweets("tw_db/t" + stre + ".txt")
        username = test_data[0]
        test_data = processing(test_data,username)
        test_data = stopword_removal_stemming.tag_pos(test_data)
        test_data = stopword_removal_stemming.stemming_stop_removal(nltk.PorterStemmer(), test_data)
        test_data_list.append(test_data)
        test_data = []
    return test_data_list

pos_data = pos_tag()

def return_keywords(data):
    final_keywords_list = []
    keywords_list = []
    keywords = []
    for row in data:
        for tweet in row:
            if len(tweet) != 0:
                for (word, tag) in tweet:
                    if tag == "NN" or tag == "NNP" or tag == "NNS":
                        if word != "@" or word != "✨" or word != "❤":
                            keywords.append(word)
            keywords_list.append(keywords)
            keywords = []
        final_keywords_list.append(keywords_list)
        keywords_list = []
    return final_keywords_list

keywords = return_keywords(pos_data)


def write_to_file(file, data):
    f = open(file, "w")
    for row in data:
        for tweet in row:
            for word in tweet:
                f.write(word)
                f.write(",")
            f.write("\n")
        f.write("\n")

write_to_file("keywords.txt", keywords)
