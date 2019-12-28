import sys

# Read file
fname = sys.argv[1]
f = open(fname, "r")
raw = f.read().split(' ')

# Clean data
a = int(raw[0])
b = int(raw[1])

def odd_sum(a, b):
    """Return the sum of all odd numbers between a and b
    >>> odd_sum(100, 200)
    7500
    """
    assert type(a) == int and type(b) == int and b > a

    # a must be odd so that we get all the odd numbers between a and b
    a = a + 1 if a % 2 == 0 else a
    return sum(list(range(a, b, 2)))

print(odd_sum(a, b))
