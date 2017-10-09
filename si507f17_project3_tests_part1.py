import unittest
from si507f17_project3_code import *

# NOTE: sample_html_of_park.html, provided, must be in your directory to be able to run all these tests

# NOTE: Running these tests on your complete code may take a minute -- especially if your code to write CSVs rewrites them every time.

###########

# REMEMBER, these tests DO NOT test everything in the project.

class Part1(unittest.TestCase):
    def setUp(self):
        self.mainpage = open("nps_gov_data.html")
        self.akfile = open("arkansas_data.html")
        self.cafile = open("california_data.html")
        self.mifile = open("michigan_data.html")

    def test_files_exist(self):
        self.assertTrue(self.mainpage.read())
        self.assertTrue(self.akfile.read())
        self.assertTrue(self.cafile.read())
        self.assertTrue(self.mifile.read())

    def tearDown(self):
        self.mainpage.close()
        self.akfile.close()
        self.cafile.close()
        self.mifile.close()

if __name__ == '__main__':
    unittest.main(verbosity=2)
