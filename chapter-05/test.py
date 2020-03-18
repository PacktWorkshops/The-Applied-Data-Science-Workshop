import unittest
import sys
import os
sys.path.append(os.path.join('..', 'tests'))
from base import BaseTests

class Test(unittest.TestCase, BaseTests):
    __test__ = True

    def setUp(self):
        self.chapter_number = 5
        super().setup_context()

    def test_workbook_library_imports(self):
        try:
            from sklearn.model_selection import train_test_split
            from sklearn.tree import DecisionTreeClassifier
            from sklearn.model_selection import cross_val_score
            from sklearn.model_selection import StratifiedKFold
            from sklearn.metrics import confusion_matrix
            from sklearn.model_selection import validation_curve
            from sklearn.decomposition import PCA
            import joblib
        except:
            print(self._import_err_msg)
            raise

    def test_data_exists(self):
        data_file_paths = [
            '../data/hr-analytics/hr_data_processed.csv',
        ]
        try:
            for file_path in data_file_paths:
                assert os.path.isfile(file_path)
        except:
            print('Some data is missing. Please download this from GitHub.')
            raise

if __name__ == '__main__':
    unittest.main()
