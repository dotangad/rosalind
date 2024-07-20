import sys

# Read file
fname = sys.argv[1]
f = open(fname, "r")
raw = f.read()

n, _ = raw.split('\n')
n = int(n)

def perm(nums, arr=[], answers=[]):
    if(len(nums) == 0):
        answers.append(arr)

    for i in nums:
        new_nums = list(filter(lambda x: x != i, nums))
        perm(new_nums, arr + [i], answers)

    return answers

def print_list_of_lists(l):
    print(len(l))
    for l_ in l:
        # Spread l_, equivalent to print(...l_) in js
        print(*l_)

def list_range(start, end):
    return list(range(start, end))

print_list_of_lists(perm(list_range(1, n + 1)))
