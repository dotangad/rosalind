import sys

# Read file
fname = sys.argv[1]
f = open(fname, "r")
raw = f.read()

# Get strings
s1, s2, _ = raw.split('\n')

def hamming(s1, s2):
    assert len(s1) == len(s2), "Strings must be equal in length"

    hamming = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            hamming += 1

    return hamming

print(hamming(s1, s2))
