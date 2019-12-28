import sys

# Read file
fname = sys.argv[1]
f = open(fname, "r")
raw = f.read()

bonds = {
    "A": "T",
    "T": "A",
    "C": "G",
    "G": "C"
}

revc = []

# Iterate over the reverse of the DNA string
for base in raw[::-1]:
    # If the character is a base and we know what
    # it bonds with, append it's complement to revc
    if base in bonds:
        revc.append(bonds[base])

# Create a string from list revc and print it out
print(''.join(revc))

