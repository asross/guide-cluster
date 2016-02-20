import csv
from .helpers import each_with_progress

class TsvAnnotator():
    def __init__(self, filename, suffix=None):
        if suffix is None:
            suffix = self.default_suffix()
        self.input_filename = filename
        self.output_filename = filename.replace(".tsv", suffix+".tsv")

    def input_fieldnames(self):
        with open(self.input_filename, 'r') as f:
            reader = csv.DictReader(f, delimiter='\t')
            row = next(reader)
        return reader.fieldnames

    def output_fieldnames(self):
        fieldnames = self.input_fieldnames()
        fieldnames.extend(self.annotation_fieldnames())
        return fieldnames

    def annotate(self, max_rows=float('inf')):
        with open(self.input_filename, 'r') as f1:
            with open(self.output_filename, 'w') as f2:
                reader = csv.DictReader(f1, delimiter='\t')
                writer = csv.DictWriter(f2, delimiter='\t', fieldnames=self.output_fieldnames())
                writer.writeheader()
                print('annotating', self.input_filename)
                for i, row in enumerate(each_with_progress(reader, 10, 100)):
                    if i >= max_rows: break
                    row.update(self.annotations(row))
                    writer.writerow(row)
                print('\ndone')

    def default_suffix(self):
        raise NotImplementedError

    def annotation_fieldnames(self):
        raise NotImplementedError

    def annotations(self, row):
        raise NotImplementedError

from .helpers import to_rna
from .mfold_wrapper import *

class MfoldAnnotator(TsvAnnotator):
    def default_suffix(self):
        return '_with_mfold'

    def annotation_fieldnames(self):
        return ['mfold_result']

    def annotations(self, row):
        mfold = MfoldWrapper(to_rna(row['spacer_seq']))
        return { 'mfold_result': mfold.fold().to_json() }

from .bowtie_wrapper import *

class BowtieAnnotator(TsvAnnotator):
    def default_suffix(self):
        return '_with_bowtie'

    def annotation_fieldnames(self):
        return ['bowtie_result']

    def annotations(self, row):
        bowtie = BowtieWrapper(row['spacer_seq'])
        return { 'bowtie_result': bowtie.search().to_json() }
