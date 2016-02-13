class Hairpin():
    def __init__(self, sequence, hairpin_indexes):
        self.sequence = sequence
        self.hairpin_indexes = hairpin_indexes

    def at(self, i, fn):
        return fn(d[i] for d in self.hairpin_indexes)

    def start_index(self):
        return self.at(0, min)

    def stem_length(self):
        return self.at(0, max) - self.at(0, min) + 1

    def loop_length(self):
        return self.at(1, min) - self.at(0, max) - 1

class NullHairpin():
    def start_index(self): return 0
    def stem_length(self): return 0
    def loop_length(self): return 0
