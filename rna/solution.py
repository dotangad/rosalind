import sys

# Read file
fname = sys.argv[1]
f = open(fname, "r")
raw = f.read()

print(raw.replace("T", "U"))
