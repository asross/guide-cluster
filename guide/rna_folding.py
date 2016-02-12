import os
import subprocess
import pdb

# This is a thin wrapper around `hybrid-ss-min` and `melt.pl` from
# http://unafold.rna.albany.edu/?q=unafold-man-pages/hybrid-ss-min
# http://unafold.rna.albany.edu/?q=unafold-man-pages/melt.pl
#
# Download the library from
# http://unafold.rna.albany.edu/?q=DINAMelt/OligoArrayAux

class GuideRnaFolding():
    def __init__(self, rna_sequence):
        self.rna_sequence = rna_sequence
        self.fold_sequence()

    def fold_sequence(self):
        file_prefix = '__tmp_guide_rna'
        fold_command = 'cd /tmp && echo {0} > {1} && melt.pl {1} > {1}.quantities'
        clean_command = 'cd /tmp && rm {}*'
        os.system(fold_command.format(self.rna_sequence, file_prefix))
        with open('/tmp/'+file_prefix+'.quantities') as f:
            self.dG, self.dH, self.dS, self.Tm = map(float, f.read().split("\n")[2].split("\t"))
        with open('/tmp/'+file_prefix+'.37.plot') as f:
            self.hairpin = [[int(i) for i in line.split("\t")] for line in f.read().split("\n")[1:-1]]
        os.system(clean_command.format(file_prefix))

    def at(self, i, fn):
        return fn(d[i] for d in self.hairpin)

    def hairpin_start_index(self):
        return self.at(0, min)

    def hairpin_stem_length(self):
        return self.at(0, max) - self.at(0, min) + 1

    def hairpin_loop_length(self):
        return self.at(1, min) - self.at(0, max) - 1
