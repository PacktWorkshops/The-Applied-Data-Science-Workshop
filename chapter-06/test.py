import unittest
import sys
import os
sys.path.append(os.path.join('..', 'tests'))
from base import BaseTests

class Test(unittest.TestCase, BaseTests):
    __test__ = True

    def setUp(self):
        self.chapter_number = 6
        super().setup_context()

    def test_workbook_library_imports(self):
        try:
            from IPython.display import HTML
            from IPython.display import IFrame
            from sklearn.preprocessing import StandardScaler
            from sklearn.cluster import KMeans
            import joblib
        except:
            print(self._import_err_msg)
            raise

if __name__ == '__main__':
    unittest.main()
