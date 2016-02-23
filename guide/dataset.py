import csv
import sys
from .datapoint import *
import numpy
import random

class GuideDataset():
    def __init__(self, filename=None, points=None):
        self.filename = filename
        self.points = points or numpy.array(list(self.each_point()))

    def each_point(self):
        with open(self.filename, 'r') as f:
            csv.field_size_limit(sys.maxsize)
            for row in csv.DictReader(f, delimiter='\t'):
                yield GuideDatapoint(row)

    def __len__(self):
        return len(self.points)

    def take(self, indices):
        return self.__class__(points=self.points.take(indices))

    def random_split(self, fraction=0.75):
        n = int(fraction * len(self))
        indices = list(range(len(self)))
        random.shuffle(indices)
        return self.take(indices[:n]), self.take(indices[n:])

    def bootstrap(self, n=None):
        return self.take([random.randrange(len(self)) for _i in range(n or len(self))])
