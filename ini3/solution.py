import sys

# Read file
fname = sys.argv[1]
f = open(fname, "r")
raw = f.read()

# Get a, b, c and d
raw = raw.split('\n')
text = raw[0]
numbers = [int(x) for x in raw[1].split(' ')]
a, b, c, d = (lambda l: (l[0], l[1], l[2], l[3]))(numbers)

print(text[a:b + 1], text[c:d + 1])
