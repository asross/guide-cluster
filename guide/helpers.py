import re

def neighbors(sequence):
    for i in range(len(sequence) - 1):
        yield sequence[i:i+2]

def to_rna(dna_sequence):
    return re.sub('T', 'U', dna_sequence)

assert(list(neighbors('AABB')) == ['AA', 'AB', 'BB'])
assert(to_rna('CTTCTCACGTGTGTATGATG') == 'CUUCUCACGUGUGUAUGAUG')
