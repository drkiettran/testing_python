import unittest
from app.main import print_hi, get_name
from test.io_util import StringIO
import sys


class testMain(unittest.TestCase):
    def setUp(self):
        self.captured_output = StringIO()
        sys.stdout = self.captured_output

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_print_hi(self):
        sys.stdin = StringIO("Gringo")
        print_hi(get_name('name:'))
        sys.stdout = sys.__stdout__
        self.assertEqual('name:Hi, Gringo\n', self.captured_output.getvalue())