import env
import unittest
from guide.rna_folding import *
from guide.dataset import *

class TestGuideRnaFolding(unittest.TestCase):
    def test_folding(self):
        folding = GuideRnaFolding('AGUGCCGCUCAAUCCAUCCC')
        self.assertEqual(3, folding.hairpin_stem_length())
        self.assertEqual(3, folding.hairpin_loop_length())
        self.assertEqual(1, folding.hairpin_start_index())
        self.assertEqual(0.2, folding.dG)
        self.assertEqual(-18, folding.dH)
        self.assertEqual(-58.7, folding.dS)
        self.assertEqual(33.6, folding.Tm)

    def test_folding_with_skips(self):
        folding = GuideRnaFolding('ACCUGUAGUUGCCGGCGUGC')
        self.assertEqual(5, folding.hairpin_stem_length())
        self.assertEqual(4, folding.hairpin_loop_length())
        self.assertEqual(4, len(folding.hairpin))

    def test_all_foldable(self):
        dataset = GuideDataset('data/example_guide_data.tsv')
        for point in dataset.each_point():
            try:
                f = point.guide_rna().folding()
            except:
                import pdb
                pdb.set_trace()

if __name__ == '__main__':
    unittest.main()
