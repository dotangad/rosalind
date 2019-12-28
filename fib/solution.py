import sys

# Read file
fname = sys.argv[1]
f = open(fname, "r")
raw = f.read()

# Clean data
s = raw.split()
n, k = int(s[0]), int(s[1])

f1 = 1
f2 = 1
for i in range(n - 2):
    f3 = f1 * k + f2
    f1, f2 = f2, f3

print(f3)
