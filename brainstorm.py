import csv
import pdb

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

with open('data/example_guide_data.tsv', 'r') as f:
    guide_data = csv.DictReader(f, delimiter='\t')
    for row in guide_data:
        pdb.set_trace()
