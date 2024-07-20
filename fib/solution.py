import sys

# Read file
fname = sys.argv[1]
f = open(fname, "r")
raw = f.read()

# Clean data
s = raw.split()
n, k = int(s[0]), int(s[1])

sub = {
    1: 1,
    2: 1
}

# range(i, j) will include i upto j but not j
for i in range(3, n + 1):
    sub[i] = sub[i - 1] + k * sub[i - 2]

print(sub[n])

# https://docs.google.com/spreadsheets/d/1LV862ZFK3hd0VoVTdUQn7q8YNB7aTNwi9OZa34j4lGI/edit?usp=sharing
