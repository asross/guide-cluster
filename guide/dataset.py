import csv
import sys
from .datapoint import *

class GuideDataset():
    def __init__(self, filename):
        self.filename = filename

    def each_point(self):
        with open(self.filename, 'r') as f:
            csv.field_size_limit(sys.maxsize)
            for row in csv.DictReader(f, delimiter='\t'):
                yield GuideDatapoint(row)

    def points(self):
        return [p for p in self.each_point()]
