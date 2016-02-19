import env
import unittest
from guide.mfold_wrapper import *
from guide.mfold_result import *

class TestMfoldWrapper(unittest.TestCase):
    def test_folding(self):
        folding = MfoldWrapper('AGUGCCGCUCAAUCCAUCCC').fold()
        self.assertEqual(3, folding.hairpin_stem_length())
        self.assertEqual(3, folding.hairpin_loop_length())
        self.assertEqual(1, folding.hairpin_start_index())
        self.assertEqual(0.2, folding.dG)
        self.assertEqual(-18, folding.dH)
        self.assertEqual(-58.7, folding.dS)
        self.assertEqual(33.6, folding.Tm)

    def test_folding_with_skips(self):
        folding = MfoldWrapper('ACCUGUAGUUGCCGGCGUGC').fold()
        self.assertEqual(5, folding.hairpin_stem_length())
        self.assertEqual(4, folding.hairpin_loop_length())
        self.assertEqual(4, len(folding.hairpin_indexes))

    def test_json(self):
        folding1 = MfoldWrapper('AGUGCCGCUCAAUCCAUCCC').fold()
        folding2 = MfoldResult.from_json(folding1.to_json())
        for attr in ['dG', 'dH', 'dS', 'Tm', 'hairpin_indexes']:
            self.assertEqual(getattr(folding1, attr), getattr(folding2, attr))

    def test_double_hairpin(self):
        folding = MfoldWrapper('CACCGGAGGGGCGCUGUAGC').fold()
        # !

if __name__ == '__main__':
    unittest.main()
