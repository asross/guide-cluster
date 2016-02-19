import env
import unittest
from guide.bowtie_wrapper import *
from guide.bowtie_result import *

class TestBowtieWrapper(unittest.TestCase):
    def test_search(self):
        search = BowtieWrapper('TCTCAGCGCGCTTTTCACCG').search()
        self.assertEqual(len(search.matches()), 20)
        match = search.exact_match()
        self.assertEqual('chr8', match.chromosome)
        self.assertEqual(18084719, match.index)
        self.assertTrue(match.is_reversed)

    def test_json(self):
        search1 = BowtieWrapper('TCTCAGCGCGCTTTTCACCG').search()
        search2 = BowtieResult.from_json(search1.to_json())
        self.assertEqual(search1._matches, search2._matches)

if __name__ == '__main__':
    unittest.main()
