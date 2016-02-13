import csv
import numpy
from .rna import *
from .helpers import activity, to_rna
from .hairpin import *

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

class GuideDatapoint():
    def __init__(self, row):
        self.row = row
        self._guide_rna = None

    def get_float(self, key):
        return float(self.row[key])

    def avg_count(self, key):
        rep1 = self.get_float(key + '_Rep1')
        rep2 = self.get_float(key + '_Rep2')
        return (rep1 + rep2) / 2.0

    def d0_d14_base_activity(self):
        return activity(self.get_float('norm_count_plasmid'), self.avg_count('norm_count_D14'))

    def d0_d7_base_activity(self):
        return activity(self.get_float('norm_count_plasmid'), self.avg_count('norm_count_D7'))

    def d7_d14_base_activity(self):
        return activity(self.avg_count('norm_count_D7'), self.avg_count('norm_count_D14'))

    def d0_d14_plx_activity(self):
        return activity(self.get_float('norm_count_plasmid'), self.avg_count('norm_count_PLX14'))

    def d0_d7_plx_activity(self):
        return activity(self.get_float('norm_count_plasmid'), self.avg_count('norm_count_PLX7'))

    def d7_d14_plx_activity(self):
        return activity(self.avg_count('norm_count_PLX7'), self.avg_count('norm_count_PLX14'))

    def rna_sequence(self):
        return to_rna(self.row['spacer_seq'])

    def rna_folding_free_energy(self):
        return self.get_float('folding_free_energy')

    def rna_folding_melt_temp(self):
        return self.get_float('folding_melt_temp')

    def has_hairpin(self):
        return self.rna_folding_free_energy() < 0

    def hairpin(self):
        if self.has_hairpin():
            return Hairpin(self.rna_sequence(), eval(self.row['folding_hairpin']))
        else:
            return NullHairpin()

    def guide_rna(self):
        if not self._guide_rna:
            self._guide_rna = GuideRna(self.row['spacer_seq'], self.row['gene_name'])
        return self._guide_rna

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
