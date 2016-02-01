import csv
import numpy
import math
from .spacer_sequence import *

"""
gene_name
spacer_id
spacer_seq
norm_count_plasmid
norm_count_D7_Rep1 norm_count_D7_Rep2
norm_count_D14_Rep1 norm_count_D14_Rep2
norm_count_PLX7_Rep1 norm_count_PLX7_Rep2
norm_count_PLX14_Rep1 norm_count_PLX14_Rep2
"""

def activity(count_before, count_after):
    count_ratio = count_before / float(count_after)
    return -math.log(count_ratio, 2)

class GuideDatapoint():
    def __init__(self, row):
        self.row = row

    def get_count(self, key):
        return float(self.row[key])

    def avg_count(self, key):
        rep1 = self.get_count(key + '_Rep1')
        rep2 = self.get_count(key + '_Rep2')
        return (rep1 + rep2) / 2.0

    def count_before(self):
        return self.get_count('norm_count_plasmid')

    def base_count_after(self):
        return self.avg_count('norm_count_D14')

    def plx_count_after(self):
        return self.avg_count('norm_count_PLX14')

    def base_activity(self):
        return activity(self.count_before(), self.base_count_after())

    def plx_activity(self):
        return activity(self.count_before(), self.plx_count_after())

    def spacer_sequence(self):
        return SpacerSequence(self.row['spacer_seq'], self.row['gene_name'])

class GuideDataset():
    def __init__(self, filename):
        self.filename = filename

    def each_point(self):
        with open(self.filename, 'r') as f:
            for row in csv.DictReader(f, delimiter='\t'):
                yield GuideDatapoint(row)

    def activities(self):
        return numpy.array([p.base_activity() for p in self.each_point()])
