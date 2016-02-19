import os
from .mfold_result import *

class MfoldWrapper():
    def __init__(self, rna_sequence):
        self.rna_sequence = rna_sequence

    def fold_command(self):
        return 'cd /tmp && echo {0} > {0} && melt.pl {0} > {0}.quantities'.format(self.rna_sequence)

    def clean_command(self):
        return 'cd /tmp && rm {}*'.format(self.rna_sequence)

    def fold(self):
        os.system(self.fold_command())
        result = MfoldResult(self.parse_quantities(), self.parse_plot())
        os.system(self.clean_command())
        return result

    def parse(self, suffix):
        with open('/tmp/'+self.rna_sequence+'.'+suffix) as f:
            text = f.read()
        return [line.split("\t") for line in text.strip().split("\n")]

    def parse_quantities(self):
        return [float(q) for q in self.parse('quantities')[2]]

    def parse_plot(self):
        return [[int(i) for i in line] for line in self.parse('37.plot')[1:]]
