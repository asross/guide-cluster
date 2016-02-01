from .constants import nucleotide_masses
from collections import Counter

class SpacerSequence():
    def __init__(self, sequence, target_gene=None):
        self.sequence = sequence
        self.target_gene = target_gene
        self.nucleotide_counts = Counter(sequence)

    def hairpin_score(self):
        return None

    def molecular_mass(self):
        # not counting extra phosphates, because it's constant
        return sum(mass * self.nucleotide_counts[n]
            for n, mass in nucleotide_masses.items())

    def gc_content(self):
        return sum(self.nucleotide_counts[n] for n in 'GC') / float(len(self))

    def reference_genome_location(self):
        return None

    def off_target_matches(self):
        return None

    def _count(self, nucleotide):
        return self.nucleotide_counts[nucleotide]

    def __len__(self):
        return len(self.sequence)
