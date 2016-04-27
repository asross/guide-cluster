import math
from .constants import rna_nucleotide_masses, five_triphosphate_mass, \
        neighbor_entropies, neighbor_enthalpies, ideal_gas_constant, \
        helix_initiation_energy, sodium_tm_adjustment, primer_concentration, \
        kelvin_to_celsius
from .helpers import neighbors, to_rna
from collections import Counter

class GuideRna():
    def __init__(self, dna_sequence):
        self.sequence = to_rna(dna_sequence)
        self.nucleotide_counts = Counter(self.sequence)
        self.neighbor_counts = Counter(neighbors(self.sequence))

    def molecular_mass(self):
        return sum(self.count(base) * mass for base, mass in rna_nucleotide_masses.items()) + five_triphosphate_mass

    def nearest_neighbor_dS(self):
        return sum(entropy * self.neighbor_counts[neighbor]
                  for neighbor, entropy in neighbor_entropies.items())

    def nearest_neighbor_dH(self):
        dH = sum(enthalpy * self.neighbor_counts[neighbor]
                for neighbor, enthalpy in neighbor_enthalpies.items())
        return dH - helix_initiation_energy

    def nearest_neighbor_Tm(self):
        dS = self.nearest_neighbor_dS()
        dH = self.nearest_neighbor_dH()
        RlnK = ideal_gas_constant * math.log(1./primer_concentration)
        return dH / (dS + RlnK) + sodium_tm_adjustment - kelvin_to_celsius

    def gc_content(self):
        return sum(self.count(base) for base in 'GC') / float(len(self))

    def count(self, base):
        return self.nucleotide_counts[base]

    def __len__(self):
        return len(self.sequence)
