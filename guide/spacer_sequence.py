from .constants import nucleotide_masses, neighbor_entropies, neighbor_enthalpies
from .helpers import neighbors
from collections import Counter
import math

class SpacerSequence():
    def __init__(self, sequence, target_gene=None):
        self.sequence = sequence
        self.target_gene = target_gene
        self.nucleotide_counts = Counter(sequence)
        self.neighbor_counts = Counter(neighbors(sequence))

    def hairpin_score(self):
        return None

    def melting_temperature(self):
        # using nearest-neighbor, following
        # http://biotools.nubic.northwestern.edu/OligoCalc.html
        assert(len(self.sequence) >= 8)
        assert(len(self.sequence) <= 20)
        assert(self.gc_content() > 0)
        # additional assumptions:
        # This apparently assumes that:
        # - len(sequence) >= 8
        # - nucleotide_counts
        dS = sum(entropy * self.neighbor_counts[nn]
                for nn, entropy in neighbor_entropies.items())
        dH = sum(enthalpy * self.neighbor_counts[nn]
                for nn, enthalpy in neighbor_enthalpies.items())
        primer_concentration = 50. * 1e-9 # moles
        sodium_concentration = 50. * 1e-3 # moles
        return (dH-3.4)/(dS+1.987*math.log(1./sodium_concentration)) - 7.21*math.log(sodium_concentration)

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
