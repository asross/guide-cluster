from .helpers import output_of
from .bowtie_result import *

class BowtieWrapper():
    def __init__(self, dna_sequence, n_mismatches=2, bowtie_index='GCA_000001405.15_GRCh38_no_alt_analysis_set'):
        self.dna_sequence = dna_sequence
        self.n_mismatches = n_mismatches
        self.bowtie_index = bowtie_index

    def search_command(self):
        return 'cd `which bowtie | xargs dirname` && bowtie -v {2} --mm -a --best {0} -c {1} --quiet'.format(self.bowtie_index, self.dna_sequence, self.n_mismatches)

    def parse(self, bowtie_output):
        if bowtie_output:
            return [self.parse_line(line) for line in bowtie_output.strip().split("\n")]
        else:
            return []

    def parse_line(self, line):
        values = line.split("\t")
        if len(values) == 7: values.append('')
        _i, direction, chromosome, index, _seq, _quals, multiplicity, mismatches = values
        mismatches = mismatches.split(',') if mismatches else []
        is_reversed = (direction == '-')
        return [is_reversed, chromosome, int(index), int(multiplicity), mismatches]

    def search(self):
        return BowtieResult(self.parse(output_of(self.search_command())))
