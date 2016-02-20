import csv
from .datapoint import *

class GuideDataset():
    def __init__(self, filename):
        self.filename = filename

    def each_point(self):
        with open(self.filename, 'r') as f:
            for row in csv.DictReader(f, delimiter='\t'):
                yield GuideDatapoint(row)

    def points(self):
        return [p for p in self.each_point()]
