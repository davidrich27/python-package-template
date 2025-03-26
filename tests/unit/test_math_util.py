from package_name.math_util import add,subtract,multiply,divide
from tests import *
from tests.helpers import *

class TestVersion(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1,5), 6)

    def test_subtract(self):
        self.assertEqual(subtract(4,7), -3)

    def test_multiply(self):
        self.assertEqual(multiply(3,7), 21)

    def test_divide(self):
        self.assertEqual(divide(3,6), 0.5)
