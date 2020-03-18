import unittest
import sys
import os
sys.path.append(os.path.join('..', 'tests'))
from base import BaseTests

class Test(unittest.TestCase, BaseTests):
    __test__ = True

    def setUp(self):
        self.chapter_number = 4
        super().setup_context()

    def test_workbook_library_imports(self):
        try:
            from sklearn.model_selection import train_test_split
            from sklearn.preprocessing import StandardScaler
            from sklearn.svm import SVC
            from sklearn.metrics import accuracy_score
            from sklearn.metrics import confusion_matrix
            from mlxtend.plotting import plot_decision_regions
            from IPython.display import display
            from sklearn.neighbors import KNeighborsClassifier
            from sklearn.ensemble import RandomForestClassifier
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
