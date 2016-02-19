import json

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

class BowtieMatch():
    def __init__(self, match):
        self.is_reversed, self.chromosome, self.index, self.multiplicity, self.mismatches = match

    def is_exact(self):
        return len(self.mismatches) == 0
