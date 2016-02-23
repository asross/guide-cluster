from .rna import *
from .helpers import activity, to_rna
from .bowtie_result import *
from .mfold_result import *

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
        self._mfold_result = None
        self._bowtie_result = None

    def get_float(self, key):
        return float(self.row[key])

    def base_count(self):
        return self.get_float('norm_count_plasmid')

    def avg_count(self, key):
        rep1 = self.get_float('norm_count_' + key + '_Rep1')
        rep2 = self.get_float('norm_count_' + key + '_Rep2')
        return (rep1 + rep2) / 2.0

    def d0_d7_base_activity(self):
        return activity(self.base_count(), self.avg_count('D7'))

    def d0_d7_plx_activity(self):
        return activity(self.base_count(), self.avg_count('PLX7'))

    def d0_d14_base_activity(self):
        return activity(self.base_count(), self.avg_count('D14'))

    def d0_d14_plx_activity(self):
        return activity(self.base_count(), self.avg_count('PLX14'))

    def d7_d14_base_activity(self):
        return activity(self.avg_count('D7'), self.avg_count('D14'))

    def d7_d14_plx_activity(self):
        return activity(self.avg_count('PLX7'), self.avg_count('PLX14'))

    def mfold_result(self):
        if not self._mfold_result:
            self._mfold_result = MfoldResult.from_json(self.row['mfold_result'])
        return self._mfold_result

    def bowtie_result(self):
        if not self._bowtie_result:
            self._bowtie_result = BowtieResult.from_json(self.row['bowtie_result'])
        return self._bowtie_result

    def guide_rna(self):
        if not self._guide_rna:
            self._guide_rna = GuideRna(self.row['spacer_seq'])
        return self._guide_rna
