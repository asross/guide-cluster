nucleotide_masses = { 'A': 313.21, 'G': 329.21, 'C': 289.18, 'T': 304.2 }

# grabbed from http://biotools.nubic.northwestern.edu/OligoCalc.html
# original source is http://www.ncbi.nlm.nih.gov/pmc/articles/PMC146261/pdf/244501.pdf

neighbor_entropies = { # cal/mol/K
'AA': 21.9,
'AC': 25.5,
'AG': 16.4,
'AT': 15.2,

'CA': 21.0,
'CC': 28.4,
'CG': 29.0,
'CT': 16.4,

'TA': 18.4,
'TC': 23.5,
'TG': 21.0,
'TT': 21.9,

'GA': 23.5,
'GC': 26.4,
'GG': 28.4,
'GT': 25.5
}

neighbor_enthalpies = { # cal/mol
'AA': 8000,
'AC': 9400,
'AG': 6600,
'AT': 5600,

'CA': 8200,
'CC': 10900,
'CG': 11800,
'CT': 6600,

'GA': 8800,
'GC': 10500,
'GG': 10900,
'GT': 9400,

'TA': 6600,
'TC': 8800,
'TG': 8200,
'TT': 8000
}

ideal_gas_constant = 1.987 # cal/(mol*K)
