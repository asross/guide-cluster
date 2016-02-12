from .constants import rna_nucleotide_masses, five_triphosphate_mass
from .helpers import neighbors, to_rna
from .rna_folding import *
from collections import Counter
import math

class GuideRna():
    def __init__(self, dna_sequence, target_gene=None):
        self.dna_sequence = dna_sequence
        self.rna_sequence = to_rna(dna_sequence)
        self.nucleotide_counts = Counter(self.rna_sequence)
        self.target_gene = target_gene
        self._folding = None
        #self.neighbor_counts = Counter(neighbors(self.rna_sequence))

    def folding(self):
        if not self._folding:
            self._folding = GuideRnaFolding(self.rna_sequence)
        return self._folding

    def molecular_mass(self):
        return sum(self.count(base) * mass for base, mass in rna_nucleotide_masses.items()) + five_triphosphate_mass

    def gc_content(self):
        return sum(self.count(base) for base in 'GC') / float(len(self))

    def reference_genome_location(self):
        return None

    def off_target_matches(self):
        return None

    def count(self, base):
        return self.nucleotide_counts[base]

    def __len__(self):
        return len(self.rna_sequence)
