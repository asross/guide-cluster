import env
import unittest
from guide.rna_sequence import *

class TestGuideRnaSequence(unittest.TestCase):
    def test_gc_content(self):
        rna_sequence = GuideRnaSequence('GCTTTAAA', '')
        self.assertEqual(rna_sequence.gc_content(), 0.25)

if __name__ == '__main__':
    unittest.main()
