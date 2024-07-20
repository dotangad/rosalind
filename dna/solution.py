import sys

# Read file
fname = sys.argv[1]
f = open(fname, "r")
raw = f.read()

def filter_fn(arr):
    """Return a function which returns all occurances
    of what's passed into it inside arr
    >>> f = filter([1, 2, 3, 1, 2, 3])
    <function f at 0xaddr>
    >>> f(1)
    [1, 1]
    """
    return lambda l: ([n for n in arr if n == l])

# Get a list of characters from the DNA string
dna_list = list(raw)
f = filter_fn(dna_list)

# Create a list of all the occurances of A, C, G and T in the DNA string
# and find it's length
bases = [len(b) for b in [f("A"), f("C"), f("G"), f("T")]]

print(*bases)
