import unittest
import sys
import os
sys.path.append(os.path.join('..', 'tests'))
from base import BaseTests

class Test(unittest.TestCase, BaseTests):
    __test__ = True

    def setUp(self):
        self.chapter_number = 1
        super().setup_context()

if __name__ == '__main__':
    unittest.main()