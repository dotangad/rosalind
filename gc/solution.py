import sys
import operator

# Read file
fname = sys.argv[1]
f = open(fname, "r")
raw = f.read()

# Clean data
dna_strings = raw.split('>')[1:]

# Create a dictionary of the DNA strings 
dna_dict = {}
for s in dna_strings:
    # s is 'Rosalind_5959\nCCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT\nATATCCATTTGTCAGCAGACACGC\n'
    s = s.split('\n')
    # s is ['Rosalind_6404', 'CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC', 'TCCCACTAATAATTCTGAGG', '']

    # The key is the first element (Rosalind_xxxx)
    # and the value is the string from joining the rest of the array
    dna_dict[s[0]] = ''.join(s[1:])

def gc(dna):
    assert type(dna) == str

    gcl = len([b for b in dna if b == "C" or b == "G"])

    return (gcl / len(dna)) * 100

# Replace the DNA string with it's GC content in dna_dict
dna_dict = {k: gc(s) for (k, s) in dna_dict.items()}
m = max(dna_dict.items(), key=operator.itemgetter(1))
print(m[0])
print(m[1])
