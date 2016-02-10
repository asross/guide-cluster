import os
import subprocess

# This is a thin wrapper around `hybrid-ss-min` and `melt.pl` from
# http://unafold.rna.albany.edu/?q=unafold-man-pages/hybrid-ss-min
# http://unafold.rna.albany.edu/?q=unafold-man-pages/melt.pl
#
# Download the library from
# http://unafold.rna.albany.edu/?q=DINAMelt/OligoArrayAux

class GuideRnaFolder():
    def __init__(self, rna_sequence):
        self.rna_sequence = rna_sequence
        if subprocess.call(['which', 'melt.pl']) == 0:
            self.fold_sequence()
        else:
            print("must install OligoArrayAux from http://unafold.rna.albany.edu/?q=DINAMelt/OligoArrayAux")

    def fold_sequence(self):
        file_prefix = '_tmp_guide_rna'
        fold_command = 'cd /tmp && echo {0} > {1} && melt.pl {1} > {1}.quantities'
        clean_command = 'cd /tmp && rm {}*'
        os.system(fold_command.format(self.rna_sequence, file_prefix))
        with open('/tmp'+file_prefix+'.quantities') as f:
            quantities = f.read()
        with open('/tmp'+file_prefix+'.37.plot') as f:
            hairpins = f.read()
        import pdb
        pdb.set_trace()
        os.system(clean_command.format(file_prefix))
