import unittest
from si507f17_project3_code import *

# NOTE: sample_html_of_park.html, provided, must be in your directory to be able to run all these tests

# NOTE: Running these tests on your complete code may take a minute -- especially if your code to write CSVs rewrites them every time.

###########

# REMEMBER, these tests DO NOT test everything in the project.

class Part2(unittest.TestCase):
    def setUp(self):
        self.f = open("sample_html_of_park.html",'r')
        self.soup_park_inst = BeautifulSoup(self.f.read(),'html.parser') # an example of 1 BeautifulSoup instance to pass into your class
        self.sample_inst = NationalSite(self.soup_park_inst)
        self.f.close()

    def test_nationalsite_constructor(self):
        self.assertIsInstance(self.sample_inst.name, str)
        self.assertTrue((self.sample_inst.type is None) or (type(self.sample_inst.type) == type("")))
        self.assertIsInstance(self.sample_inst.description, str)
        self.assertIsInstance(self.sample_inst.location, str)

    def test_nationalsite_get_address(self):
        self.assertIsInstance(self.sample_inst.get_mailing_address(),str)

    def test_nationalsite_string(self):
        self.assertEqual(self.sample_inst.__str__(), "Isle Royale | Houghton, MI")

    def test_nationalsite_contains(self):
        self.assertTrue("le" in self.sample_inst)
        self.assertTrue("Yosemite" not in self.sample_inst)

if __name__ == '__main__':
    unittest.main(verbosity=2)
