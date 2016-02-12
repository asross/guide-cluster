import env
import unittest
from guide.rna import *

class TestGuideRna(unittest.TestCase):
    def test_gc_content(self):
        gRNA = GuideRna('GCUUUAAA')
        self.assertEqual(gRNA.gc_content(), 0.25)

    def test_molecular_mass(self):
        # matches what is returned by
        # http://biotools.nubic.northwestern.edu/OligoCalc.html
        # and http://mods.rna.albany.edu/masspec/Mongo-Oligo
        # without taking into account extra phosphates.
        gRNA = GuideRna('AGUGCCGCUCAAUCCAUCCC')
        self.assertEqual(round(gRNA.molecular_mass()), 6483)

if __name__ == '__main__':
    unittest.main()
