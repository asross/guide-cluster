from .helpers import output_of
from .bowtie_result import *

# human genome index
bowtie_index = 'GCA_000001405.15_GRCh38_no_alt_analysis_set'

class BowtieWrapper():
    def __init__(self, dna_sequence):
        self.dna_sequence = dna_sequence

    def search_command(self):
        return 'cd `which bowtie | xargs dirname` && bowtie -v 3 -a --best {0} -c {1} --quiet'.format(bowtie_index, self.dna_sequence)

    def parse(self, bowtie_output):
        return [self.parse_line(line) for line in bowtie_output.strip().split("\n")]

    def parse_line(self, line):
        _i, direction, chromosome, index, _seq, _quals, multiplicity, mismatches = line.split("\t")
        mismatches = mismatches.split(',') if mismatches else []
        is_reversed = (direction == '-')
        return [is_reversed, chromosome, int(index), int(multiplicity), mismatches]

    def search(self):
        return BowtieResult(self.parse(output_of(self.search_command())))
