import unittest
import sys
import os
sys.path.append(os.path.join('..', 'tests'))
from base import BaseTests

class Test(unittest.TestCase, BaseTests):
    __test__ = True

    def setUp(self):
        self.chapter_number = 2
        super().setup_context()

    def test_workbook_library_imports(self):
        try:
            from sklearn import datasets
            from sklearn.utils import Bunch
            from sklearn.linear_model import LinearRegression
            from sklearn.metrics import mean_squared_error
            from sklearn.preprocessing import PolynomialFeatures
        except:
            print(self._import_err_msg)
            raise

if __name__ == '__main__':
    unittest.main()
