import re
def read_user_from_file():
    f = open("tw_db/t0.txt", "r")
    data = []
    for line in f:
        data.append(line)
    return data
"""
Function to remove the usernames of the user which are not required for further processing
"""
def remove_username(username, data):
    data_at = []
    for item in data:
        if username in item:
            item = item.replace(username, "")
        data_at.append(item)
    return data_at


"""
Function to remove the emoji patterns which are not required for further processing
"""

def remove_emoji(emoji_pattern, data):
    data_at = []
    for item in data:
        item = emoji_pattern.sub(r'', item)
        data_at.append(item)
    return data_at

"""
Function to remove the symbols which are not required for further processing
"""

def remove(symbol, data):
    data_at = []
    for item in data:
        if symbol in item:
            item = item.replace(symbol, "")
        data_at.append(item)
    return data_at

"""
Function to remove the links which are not required for further processing
"""

def remove_links(data):
    data1 = []
    for line in data:
        data1.append(re.sub(r"\bhttps:\/\/t\.co\/\w*\b", "", line))
    return data1
