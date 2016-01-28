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


"""
GuideDataMunger
    => GuideDataset

GuideDataMunger will take a dataset file and a reference genome file, and it
will output a dataset with extra features such as hairpin presence, mass,
melting temperature, location in the reference genome, presence of off-target
matches, etc.

GuideActivityClusterer

GuideActivityClusterer will take a GuideDataset and output an object with
information about clusters in the activity of the guides. It may be able to
return, e.g., a list of genes whose knockout seems to affect the cell in a
meaningful way. It will be able to plot a summary of its results

GuideDecisionTreeClassifier(GuideClassifier)

GuideDecisionTree will take a GuideDataset (potentially a subset) and output
a decision tree that can predict the activity of future guides. It will also
be printable in a way that can be interpreted, hopefully common-sensically.

GuideDNNClassifier(GuideClassifier)

GuideDNNClassifier will take (some set of) the features of a GuideDataset and
train a DNN to predict the activity of future guides. It will hopefully perform
better that the GuideDecisionTree even if its underlying logic is more opaque.

GuideClassifier

GuideClassifier will be able to output various metrics about how well it performed for
a given training/test set.

(maybe sub classifier for regressor -- or if the clustering permits, make it boolean)

All of these will probably make sense as part of an iPython notebook with inline plots.

Another option is to have a script which outputs (deterministically?) some CSV/JSON files
and loads them into a webpage for some D3ing.
"""
