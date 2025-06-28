import unittest

from Math.Tensor import Tensor


class TensorTest(unittest.TestCase):

    def test_dot_same(self):
        a = Tensor([[[1, 1], [1, 1]], [[1, 1], [1, 1]]])
        b = Tensor([[[1, 1], [1, 1]], [[1, 1], [1, 1]]])
        a.multiply(b)

    def test_dot_different(self):
        a = Tensor([[[1, 1, 1], [1, 1, 1]]])
        b = Tensor([[[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]])
        a.multiply(b)

if __name__ == '__main__':
    unittest.main()
