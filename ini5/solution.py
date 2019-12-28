import sys

# Read file
fname = sys.argv[1]
f = open(fname, "r")
raw = f.read()

print('\n'.join(raw.split('\n')[1:-1:2]))
