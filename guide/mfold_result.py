import json

class MfoldResult():
    def __init__(self, quantities, hairpin_indexes):
        self.dG, self.dH, self.dS, self.Tm = quantities
        self.hairpin_indexes = hairpin_indexes

    def to_json(self):
        return json.dumps([[self.dG, self.dH, self.dS, self.Tm], self.hairpin_indexes])

    @classmethod
    def from_json(cls, blob):
        return cls(*json.loads(blob))

    def indicates_hairpin(self):
        return self.dG < 0

    def at(self, i, fn):
        return fn(d[i] for d in self.hairpin_indexes)

    def hairpin_start_index(self):
        return self.at(0, min)

    def hairpin_stem_length(self):
        return self.at(0, max) - self.at(0, min) + 1

    def hairpin_loop_length(self):
        return self.at(1, min) - self.at(0, max) - 1
