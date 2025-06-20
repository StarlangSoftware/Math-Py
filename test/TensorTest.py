import unittest

from Math.Tensor import Tensor


class MyTestCase(unittest.TestCase):

    def test_dot_same(self):
        a = Tensor([[[1, 1], [1, 1]], [[1, 1], [1, 1]]])
        b = Tensor([[[1, 1], [1, 1]], [[1, 1], [1, 1]]])
        a.dot(b)

    def test_dot_different(self):
        a = Tensor([[[1, 1, 1], [1, 1, 1]]])
        b = Tensor([[[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]])
        a.dot(b)

if __name__ == '__main__':
    unittest.main()
