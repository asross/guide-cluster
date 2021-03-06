import json

class Hairpin():
    def __init__(self, indexes):
        self.indexes = indexes

    def at(self, i, fn):
        return fn(d[i] for d in self.indexes)

    def start_index(self):
        return self.at(0, min)

    def stem_length(self):
        return self.at(0, max) - self.at(0, min) + 1

    def loop_length(self):
        return self.at(1, min) - self.at(0, max) - 1

    def __len__(self):
        return self.stem_length()

class MfoldResult():
    def __init__(self, quantities, hairpin_indexes):
        self.dG, self.dH, self.dS, self.Tm = quantities
        self.hairpin_indexes = hairpin_indexes

    def to_json(self):
        return json.dumps([[self.dG, self.dH, self.dS, self.Tm], self.hairpin_indexes])

    @classmethod
    def from_json(cls, blob):
        return cls(*json.loads(blob))

    def hairpins(self):
        if not self.hairpin_indexes: return []
        hairpins = []
        hairpin = [self.hairpin_indexes[0]]
        for indexes in self.hairpin_indexes[1:]:
            if indexes[0] > hairpin[0][0] and indexes[1] < hairpin[0][1]:
                hairpin.append(indexes)
            else:
                hairpins.append(Hairpin(hairpin))
                hairpin = [indexes]
        hairpins.append(Hairpin(hairpin))
        return hairpins

    def longest_hairpin(self):
        if not self.hairpin_indexes:
            return None
        else:
            return max(self.hairpins(), key=len)

    def indicates_hairpin(self):
        return self.dG < 0 and self.hairpin_indexes != None

    def longest_hairpin_stem_length(self):
        if not self.indicates_hairpin(): return 0
        return max([h.stem_length() for h in self.hairpins()])

    def longest_hairpin_loop_length(self):
        if not self.indicates_hairpin(): return 0
        return max([h.loop_length() for h in self.hairpins()])

    def longest_hairpin_start_index(self):
        if not self.indicates_hairpin(): return -1
        return self.longest_hairpin().start_index()

    def hairpin_count(self):
        if not self.indicates_hairpin(): return 0
        return len(self.hairpins())
