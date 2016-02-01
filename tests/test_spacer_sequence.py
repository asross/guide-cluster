import env
import unittest
from guide.spacer_sequence import *

class TestSpacerSequence(unittest.TestCase):
    def test_gc_content(self):
        sequence = SpacerSequence('GCTTTAAA')
        self.assertEqual(sequence.gc_content(), 0.25)

    def test_molecular_mass(self):
        # matches what is returned by
        # http://biotools.nubic.northwestern.edu/OligoCalc.html
        # and http://mods.rna.albany.edu/masspec/Mongo-Oligo
        # without taking into account extra phosphates.
        sequence = SpacerSequence('AGTGCCGCTCAATCCATCCC')
        self.assertEqual(round(sequence.molecular_mass() - 61.96), 5998)

    def test_melting_temperature(self):
        sequence = SpacerSequence('AGTGCCGCTCAATCCATCCC')
        self.assertEqual(round(sequence.melting_temperature(), 1), 56.1)

if __name__ == '__main__':
    unittest.main()
