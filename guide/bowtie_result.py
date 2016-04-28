import json
from collections import Counter

class BowtieResult():
    def __init__(self, matches):
        self._matches = matches

    def to_json(self):
        return json.dumps(self._matches)

    @classmethod
    def from_json(cls, blob):
        return cls(json.loads(blob))

    def matches(self):
        return [BowtieMatch(m) for m in self._matches]

    def exact_match(self):
        matches = self.matches()
        if len(matches) > 0 and matches[0].is_exact():
            if len(matches) == 1 or not matches[1].is_exact():
                return matches[0]

    def mismatch_counts(self):
        matches = self.matches()[1:]
        return Counter(len(m.differences) for m in matches)

    def same_chromosome_mismatch_counts(self):
        matches = self.matches()
        chromosome = matches[0].chromosome
        return Counter(len(m.differences) for m in matches[1:] if m.chromosome == chromosome)

class BowtieMatch():
    def __init__(self, match):
        self.is_reversed, self.chromosome, self.index, self.multiplicity, self.differences = match

    def is_exact(self):
        return len(self.differences) == 0
