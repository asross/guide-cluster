from guide.annotators import *

bt_annotator = BowtieAnnotator('data/example_guide_data.tsv')
bt_annotator.annotate()

mf_annotator = MfoldAnnotator(bt_annotator.output_filename)
mf_annotator.annotate()
