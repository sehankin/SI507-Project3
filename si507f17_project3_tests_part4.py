import unittest
from si507f17_project3_code import *

# NOTE: sample_html_of_park.html, provided, must be in your directory to be able to run all these tests

# NOTE: Running these tests on your complete code may take a minute -- especially if your code to write CSVs rewrites them every time.

###########

# REMEMBER, these tests DO NOT test everything in the project.

class Part4(unittest.TestCase):

    def setUp(self):
        self.ak = open("arkansas.csv",'r')
        self.mi = open("michigan.csv",'r')
        self.ca = open("california.csv",'r')

    def test_csv_files_exist(self):
        self.assertTrue(self.ak.read())
        self.assertTrue(self.ca.read())
        self.assertTrue(self.mi.read())

    def tearDown(self):
        self.ak.close()
        self.ca.close()
        self.mi.close()

if __name__ == '__main__':
    unittest.main(verbosity=2)
