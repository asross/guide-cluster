from .constants import nucleotide_masses, neighbor_entropies, neighbor_enthalpies, ideal_gas_constant
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
        return sum(enthalpy * self.neighbor_counts[nn]
                for nn, enthalpy in neighbor_enthalpies.items())

    def melting_temperature(self):
        # using nearest-neighbor, following
        # http://biotools.nubic.northwestern.edu/OligoCalc.html
        assert(len(self.sequence) >= 8)
        assert(len(self.sequence) <= 20)
        assert(self.gc_content() > 0)

        dS = self.melting_entropy_change()
        dH = self.melting_enthalpy_change()
        primer_concentration = 50. * 1e-9 # mol
        helix_initiation_free_energy_change = 3400 # cal/mol
        self_complementary_free_energy_change = 0 # for now, should be 400 sometimes

        # this is constant and could be ignored, but i want the numbers to match
        sodium_concentration = 50. * 1e-3 # mol
        sodium_tm_adjustment = 7.21 * math.log(sodium_concentration)

        base_tm_calculation = (dH - helix_initiation_free_energy_change) \
            / (dS + ideal_gas_constant * math.log(1./primer_concentration))

        return base_tm_calculation + sodium_tm_adjustment - 272.9

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
