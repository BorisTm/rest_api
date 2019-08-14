import unittest
import unittest.mock
import my_g


def add(x, y):
    if x == 42:
        raise ValueError
    return x + y


class TestAdd(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5, 'Error')

    @unittest.mock.patch('my_g.f')
    def test_g(self, a):
        a.side_effect = 2, 3
        self.assertEqual(my_g.g(2), 4)
        self.assertEqual(my_g.g(3), 9)