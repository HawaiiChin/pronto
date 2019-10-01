import itertools
import os
import unittest

import pronto
from pronto.term import Term, _TermData

from .utils import DATADIR



class TestTerm(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.ms = pronto.Ontology(os.path.join(DATADIR, "ms.obo.xz"))

    def test_properties(self):
        for t in _TermData.__slots__:
            self.assertTrue(hasattr(Term, t), f"no property for {t}")

    def test_subclasses(self):
        term = self.ms['MS:1003025']
        self.assertSetEqual(
            {sub.id for sub in term.subclasses()},
            {'MS:1003025', 'MS:1003026', 'MS:1003027', 'MS:1003021', 'MS:1003022'},
        )

    def test_subclasses_distance(self):
        term = self.ms['MS:1000031']
        self.assertSetEqual(set(term.subclasses(0)), {term})
        self.assertSetEqual(
            {sub.id for sub in term.subclasses(1)},
            {
                'MS:1000031', 'MS:1000490', 'MS:1000495', 'MS:1000122',
                'MS:1000491', 'MS:1000488', 'MS:1001800', 'MS:1000121',
                'MS:1000124', 'MS:1000483', 'MS:1000489', 'MS:1000126',
            }
        )

    def test_subclasses_uniqueness(self):
        for term in itertools.islice(self.ms.terms(), 10):
            subclasses = list(term.subclasses())
            self.assertCountEqual(subclasses, set(subclasses))

    def test_superclasses(self):
        term = self.ms['MS:1000200']
        self.assertSetEqual(
            {sup.id for sup in term.superclasses()},
            {'MS:1000200', 'MS:1000123', 'MS:1000489', 'MS:1000031'},
        )

    def test_superclasses_distance(self):
        term = self.ms['MS:1000200']
        scls = ['MS:1000200', 'MS:1000123', 'MS:1000489', 'MS:1000031']
        for i in range(len(scls)):
            self.assertSetEqual(
                {sup.id for sup in term.superclasses(i)},
                set(scls[:i+1])
            )

    def test_superclasses_uniqueness(self):
        for term in self.ms.terms():
            superclasses = list(term.superclasses())
            self.assertCountEqual(superclasses, set(superclasses))