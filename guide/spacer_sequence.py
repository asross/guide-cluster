from .constants import nucleotide_masses, neighbor_entropies, \
    neighbor_enthalpies, ideal_gas_constant, helix_initiation_energy, \
    sodium_melting_temperature_adjustment
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

    def melting_entropy_change(self):
        return sum(entropy * self.neighbor_counts[nn]
                for nn, entropy in neighbor_entropies.items())

    def melting_enthalpy_change(self):
        dH = sum(enthalpy * self.neighbor_counts[nn]
                for nn, enthalpy in neighbor_enthalpies.items())
        return dH - helix_initiation_energy

    def melting_temperature(self, primer_concentration=5e-8):
        # using nearest-neighbor, following
        # http://biotools.nubic.northwestern.edu/OligoCalc.html
        assert(len(self.sequence) >= 8)
        assert(len(self.sequence) <= 20)
        assert(self.gc_content() > 0)
        dS = self.melting_entropy_change()
        dH = self.melting_enthalpy_change()
        dG = ideal_gas_constant * math.log(1./primer_concentration)
        return dH / (dS + dG) + sodium_melting_temperature_adjustment

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
