from .constants import nucleotide_masses
from .helpers import neighbors, to_rna
from .rna_folder import GuideRnaFolder
from collections import Counter
import math

class GuideRnaSequence():
    def __init__(self, dna_sequence, target_gene=None):
        self.dna_sequence = dna_sequence
        self.rna_sequence = to_rna(dna_sequence)
        self.base_counts = Counter(self.rna_sequence)
        self.target_gene = target_gene
        #self.neighbor_counts = Counter(neighbors(self.rna_sequence))

    def rna_folder(self):
        if not self.rna_folder:
            self.rna_folder = GuideRnaFolder(self.rna_sequence)
        return self.rna_folder

    def molecular_mass(self):
        return sum(self.count(base) * mass for base, mass in nucleotide_masses.items())

    def gc_content(self):
        return sum(self.count(base) for base in 'GC') / float(len(self))

    def reference_genome_location(self):
        return None

    def off_target_matches(self):
        return None

    def count(self, base):
        return self.nucleotide_counts[base]

    def __len__(self):
        return len(self.sequence)
