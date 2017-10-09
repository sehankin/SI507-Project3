import unittest
from si507f17_project3_code import *

# NOTE: sample_html_of_park.html, provided, must be in your directory to be able to run all these tests

# NOTE: Running these tests on your complete code may take a minute -- especially if your code to write CSVs rewrites them every time.

###########

# REMEMBER, these tests DO NOT test everything in the project.

class Part3(unittest.TestCase):

    def setUp(self):
        pass

    def test_list_vars(self):
        self.assertIsInstance(arkansas_natl_sites,list)
        self.assertIsInstance(california_natl_sites, list)
        self.assertIsInstance(michigan_natl_sites, list)

    def test_list_elem_types(self):
        self.assertIsInstance(arkansas_natl_sites[0],NationalSite)
        self.assertIsInstance(arkansas_natl_sites[-1],NationalSite)
        self.assertIsInstance(california_natl_sites[0],NationalSite)
        self.assertIsInstance(michigan_natl_sites[0],NationalSite)

if __name__ == '__main__':
    unittest.main(verbosity=2)
