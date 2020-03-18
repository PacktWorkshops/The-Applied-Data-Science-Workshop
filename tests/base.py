import unittest

class BaseTests():
    __test__ = False

    def setup_context(self):
        self.github_repo = 'PacktWorkshops/The-Applied-Data-Science-Workshop'
        self.notebook_remote_file = (
            'https://raw.githubusercontent.com/{repo}/master/chapter-0{chapter}/chapter_{chapter}_workbook.ipynb'.format(
                repo=self.github_repo,
                chapter=self.chapter_number,
            )
        )
        self.notebook_local_file = self.notebook_remote_file.split('/')[-1]

    def test_notebook_exists(self):
        import os
        try:
            assert os.path.isfile(self.notebook_local_file)
        except:
            print(
                'Local workbook not found ({})'.format(self.notebook_local_file)
            )
            raise

    def test_notebook_matches_remote(self):
        import requests
        notebook_remote_text = requests.get(self.notebook_remote_file).text.strip()
        with open(self.notebook_local_file, 'r') as f:
            notebook_local_text = f.read().strip()
        try:
            assert notebook_local_text == notebook_remote_text
        except:
            print(
                'Local workbook ({local}) differs from that on GitHub '
                '(https://github.com/{remote}). '
                'Either the GitHub repository has been updated or you have '
                'made changes to your local workbook.'.format(
                    local=self.notebook_local_file,
                    remote=self.github_repo,
                )
            )
            raise

    def test_ipython_installed(self):
        try:
            import IPython
        except:
            print(
                'IPython needs to be installed to run Jupyter Notebooks. '
                'Please install "jupyter notebook" or "jupyter lab". These '
                'are included in the Anaconda Python distribution, or can be '
                'installed with pip.'
            )
            raise

    @property
    def _import_err_msg(self):
        return (
            'Some library dependencies failed to load. These are included '
            'in the Anaconda Python distribution, or can be installed with '
            'pip.'
        )

    def test_core_library_imports(self):
        try:
            import numpy as np
            import pandas as pd
            import sklearn
            import requests
            from bs4 import BeautifulSoup
            import matplotlib.pyplot as plt
            import seaborn as sns
        except:
            print(self._import_err_msg)
            raise