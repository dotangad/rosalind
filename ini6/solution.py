import sys

# Read file
fname = sys.argv[1]
f = open(fname, "r")
raw = f.read()

def count_words(raw):
    "Count all the words in a given string"
    assert type(raw) == str

    words_list = raw.split()
    words = dict()

    # Iterate over raw words
    for word in words_list:
        if word in words:
            words[word] = words[word] + 1
        else:
            words[word] = 1

    return words

for key, value in count_words(raw).items():
    print(key, value)

