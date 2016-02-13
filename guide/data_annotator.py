import csv
from .helpers import to_rna
from .rna_folding import *

fieldnames = [
'gene_name',
'spacer_id',
'spacer_seq',
'norm_count_plasmid',
'norm_count_D7_Rep1',
'norm_count_D7_Rep2',
'norm_count_D14_Rep1',
'norm_count_D14_Rep2',
'norm_count_PLX7_Rep1',
'norm_count_PLX7_Rep2',
'norm_count_PLX14_Rep1',
'norm_count_PLX14_Rep2',
'folding_free_energy',
'folding_enthalpy',
'folding_entropy',
'folding_melt_temp',
'folding_hairpin'
]

class GuideDataAnnotator():
    def __init__(self, filename):
        self.input_filename = filename
        self.output_filename = filename.replace(".tsv", "_annotated.tsv")

    def annotate(self):
        with open(self.input_filename, 'r') as fin:
            with open(self.output_filename, 'w') as fout:
                reader = csv.DictReader(fin, delimiter='\t')
                writer = csv.DictWriter(fout, fieldnames=fieldnames, delimiter='\t')
                writer.writeheader()
                i = 0
                for row in reader:
                    if i % 1000 == 0:
                        print(i)
                    i += 1
                    writer.writerow(self.annotate_row(row))

    def annotate_row(self, row):
        rna = to_rna(row['spacer_seq'])
        folding = GuideRnaFolding(rna)
        row.update({
            'folding_free_energy': folding.dG,
            'folding_enthalpy': folding.dH,
            'folding_entropy': folding.dS,
            'folding_melt_temp': folding.Tm,
            'folding_hairpin': folding.hairpin
        })
        return row


