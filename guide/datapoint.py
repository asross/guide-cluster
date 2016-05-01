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

    # Features

    # Raw sequence features
    def gc_content(self): return self.guide_rna().gc_content()
    def dna_starts_with_g(self): return int(self.row['spacer_seq'][0] == 'G')
    def dna_starts_with_gg(self): return int(self.row['spacer_seq'][0:2] == 'GG')
    def dna_starts_with_atg(self): return int(self.row['spacer_seq'][0:3] == 'ATG')
    def dna_contains_gg(self): return int('GG' in self.row['spacer_seq'])
    def dna_contains_atg(self): return int('ATG' in self.row['spacer_seq'])

    # OligoCalc features
    def molecular_mass(self): return self.guide_rna().molecular_mass()
    def nearest_neighbor_dS(self): return self.guide_rna().nearest_neighbor_dS()
    def nearest_neighbor_dH(self): return self.guide_rna().nearest_neighbor_dH() / 1000
    def nearest_neighbor_Tm(self): return self.guide_rna().nearest_neighbor_Tm()

    # mfold thermodynamic features
    def mfold_dS(self): return self.mfold_result().dS
    def mfold_dH(self): return self.mfold_result().dH
    def mfold_dG(self): return self.mfold_result().dG
    def mfold_Tm(self): return self.mfold_result().Tm

    # mfold hairpin features
    def hairpin_stem_length(self): return self.mfold_result().longest_hairpin_stem_length()
    def hairpin_loop_length(self): return self.mfold_result().longest_hairpin_loop_length()
    def hairpin_start_index(self): return self.mfold_result().longest_hairpin_start_index()
    def hairpin_count(self): return self.mfold_result().hairpin_count()

    # Bowtie features
    def bowtie_hit_index(self): return self.bowtie_result().index()
    def bowtie_hits_1_mm(self): return self.bowtie_result().mismatch_counts()[1]
    def bowtie_hit_chromosome(self):
        return self.bowtie_result().chromosome_number()
    def bowtie_hits_same_chromosome_1_mm(self):
        return self.bowtie_result().same_chromosome_mismatch_counts()[1]
    def bowtie_hits_1_or_2_mms(self):
        counts = self.bowtie_result().mismatch_counts()
        return counts[1] + counts[2]
    def bowtie_hits_same_chromosome_1_or_2_mms(self):
        counts = self.bowtie_result().same_chromosome_mismatch_counts()
        return counts[1] + counts[2]

feature_units = {
'molecular_mass':       'g/mol',
'gc_content':           'fraction',
'dna_starts_with_g':    'False/True',
'dna_starts_with_gg':   'False/True',
'dna_starts_with_atg':  'False/True',
'dna_contains_gg':      'False/True',
'dna_contains_atg':     'False/True',
'nearest_neighbor_dS':  'cal/mol/K',
'nearest_neighbor_dH':  'kcal/mol',
'nearest_neighbor_Tm':  'C',
'mfold_dS':             'J/mol/K',
'mfold_dH':             'kcal/mol',
'mfold_dG':             'kcal/mol',
'mfold_Tm':             'C',
'hairpin_count':        '# hairpins',
'hairpin_start_index':  'position in sequence',
'hairpin_stem_length':  'bp',
'hairpin_loop_length':  'bp',
'bowtie_hit_chromosome':                    'chromosome no.',
'bowtie_hit_index':                         'position in chromosome',
'bowtie_hits_1_mm':                         '# hits',
'bowtie_hits_1_or_2_mms':                   '# hits',
'bowtie_hits_same_chromosome_1_mm':         '# hits',
'bowtie_hits_same_chromosome_1_or_2_mms':   '# hits'
}
