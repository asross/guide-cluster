class GuideRnaSequence():
    def __init__(self, sequence, gene):
        self.sequence = sequence
        self.gene = gene

    def hairpin_score(self):
        return None

    def melting_temperature(self):
        return None

    def mass(self):
        return None

    def reference_genome_location(self):
        return None

    def off_target_matches(self):
        return None

    def gc_content(self):
        return sum(s in 'GC' for s in self.sequence) / float(len(self))

    def __len__(self):
        return len(self.sequence)
