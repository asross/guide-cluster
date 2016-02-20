from .constants import rna_nucleotide_masses, five_triphosphate_mass
from .helpers import neighbors, to_rna
from collections import Counter

class GuideRna():
    def __init__(self, dna_sequence):
        self.sequence = to_rna(dna_sequence)
        self.nucleotide_counts = Counter(self.sequence)
        self.neighbor_counts = Counter(neighbors(self.sequence))

    def molecular_mass(self):
        return sum(self.count(base) * mass for base, mass in rna_nucleotide_masses.items()) + five_triphosphate_mass

    def gc_content(self):
        return sum(self.count(base) for base in 'GC') / float(len(self))

    def count(self, base):
        return self.nucleotide_counts[base]

    def __len__(self):
        return len(self.sequence)
