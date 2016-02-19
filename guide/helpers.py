import re
import math
import subprocess

def output_of(cmd):
    return subprocess.check_output(cmd, shell=True).decode('utf-8')

def neighbors(sequence):
    for i in range(len(sequence) - 1):
        yield sequence[i:i+2]

def to_rna(dna_sequence):
    return re.sub('T', 'U', dna_sequence)

def activity(count_before, count_after):
    count_ratio = count_before / float(count_after)
    return -math.log(count_ratio, 2)

assert(list(neighbors('AABB')) == ['AA', 'AB', 'BB'])
assert(to_rna('CTTCTCACGTGTGTATGATG') == 'CUUCUCACGUGUGUAUGAUG')
