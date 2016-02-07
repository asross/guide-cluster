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

    def d0_d14_base_activity(self):
        return activity(self.get_count('norm_count_plasmid'), self.avg_count('norm_count_D14'))
    def d0_d7_base_activity(self):
        return activity(self.get_count('norm_count_plasmid'), self.avg_count('norm_count_D7'))
    def d7_d14_base_activity(self):
        return activity(self.avg_count('norm_count_D7'), self.avg_count('norm_count_D14'))
    def d0_d14_plx_activity(self):
        return activity(self.get_count('norm_count_plasmid'), self.avg_count('norm_count_PLX14'))
    def d0_d7_plx_activity(self):
        return activity(self.get_count('norm_count_plasmid'), self.avg_count('norm_count_PLX7'))
    def d7_d14_plx_activity(self):
        return activity(self.avg_count('norm_count_PLX7'), self.avg_count('norm_count_PLX14'))

    def spacer_sequence(self):
        return SpacerSequence(self.row['spacer_seq'], self.row['gene_name'])

class GuideDataset():
    def __init__(self, filename):
        self.filename = filename

    def each_point(self):
        with open(self.filename, 'r') as f:
            for row in csv.DictReader(f, delimiter='\t'):
                yield GuideDatapoint(row)

    def call_each(self, key):
        return numpy.array([getattr(p, key)() for p in self.each_point()])

    def get_each(self, key):
        return numpy.array([p.row[key] for p in self.each_point()])
