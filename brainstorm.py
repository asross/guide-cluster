import csv
import pdb
from collections import Counter
import numpy
from sklearn.decomposition import PCA

# norm_count_D7_Rep1
# norm_count_D7_Rep2
# norm_count_D14_Rep1
# norm_count_D14_Rep2
# norm_count PLX7_Rep1
# norm_count_PLX7_Rep2
# norm_count_PLX14_Rep1
# norm_count_PLX14_Rep2
# norm_count_plasmid

# spacer_id
# spacer_seq

# gene_name

"""
the norm counts represent frequency in the population

comparing D14 to Dplasmid or D14 to D7 can give a sense of the activity
that's what we're looking to cluster

if we were going to predict the activity of a guide, what metrics about
the DNA sequence would actually matter?

there might be certain properties of the sequence that make them suitable
or unsuitable for use in CRISPr.

there might be certain properties of the *reference genome* that make the
sequences unsuitable.

The off-target scores are one important feature (?) maybe
"""

base_numbers = { 'C': 0, 'G': 1, 'A': 2, 'T': 3 }
base_lists = { 'C': [0, 0], 'G': [0, 1], 'A': [1, 0], 'T': [1, 1] }

with open('data/example_guide_data.tsv', 'r') as f:
    guide_data = csv.DictReader(f, delimiter='\t')
    sequences = [row['spacer_seq'] for row in guide_data]
    #counts = Counter()
    #for seq in sequences:
        #for base in seq:
            #counts[base] += 1
    X = numpy.array([[n for base in seq for n in base_lists[base]] for seq in sequences])
    pca = PCA(n_components='mle')
    pca.fit(X)
    print(pca.explained_variance_ratio_) 

    pdb.set_trace()
