import math

# grabbed from http://biotools.nubic.northwestern.edu/OligoCalc.html
five_triphosphate_mass = 159 # g/mol
rna_nucleotide_masses = { # g/mol
'A': 329.21, 'U': 306.17, 'C': 305.18, 'G': 345.21
}
neighbor_entropies = { # cal/mol/K
'AA': 19.0,
'AC': 26.2,
'AG': 19.2,
'AU': 26.7,
'CA': 26.9,
'CC': 29.7,
'CG': 26.7,
'CU': 27.1,
'GA': 32.5,
'GC': 36.9,
'GG': 32.7,
'GU': 29.5,
'UA': 20.5,
'UC': 35.5,
'UG': 27.8,
'UU': 18.4
}
neighbor_enthalpies = { # cal/mol
'AA': 6820.0,
'AC': 10200.0,
'AG': 7600.0,
'AU': 9380.0,
'CA': 10440.0,
'CC': 12200.0,
'CG': 10640.0,
'CU': 10480.0,
'GA': 12440.0,
'GC': 14880.0,
'GG': 13390.0,
'GU': 11400.0,
'UA': 7690.0,
'UC': 13300.0,
'UG': 10500.0,
'UU': 6600.0
}
ideal_gas_constant = 1.987 # cal/(mol*K)
helix_initiation_energy = 3400 # cal
sodium_concentration = 5e-2 # mol
primer_concentration = 5e-8 # mol
sodium_tm_adjustment = 7.21 * math.log(sodium_concentration) # K
kelvin_to_celsius = 273.15 # K
