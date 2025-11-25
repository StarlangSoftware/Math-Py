import unittest

from Math.Tensor import Tensor


class TensorTest(unittest.TestCase):

    def test_inferred_shape(self):
        a = Tensor([[1.0, 2.0], [3.0, 4.0]])
        self.assertEqual((2, 2), a.getShape())

    def test_shape(self):
        a = Tensor([1.0, 2.0, 3.0])
        self.assertEqual((3, ), a.getShape())

    def test_transpose_no_axes(self):
        a = Tensor([[1.0, 2.0], [3.0, 4.0]])
        b = a.transpose()
        self.assertEqual([1.0, 3.0, 2.0, 4.0], b.getData())

    def test_transpose_with_axes(self):
        a = Tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
        b = a.transpose((1, 0))
        self.assertEqual([1.0, 4.0, 2.0, 5.0, 3.0, 6.0], b.getData())

    def test_broadcast_to_valid(self):
        a = Tensor([1.0, 2.0], (1, 2))
        b = a.broadcast_to((2, 2))
        self.assertEqual([1.0, 2.0, 1.0, 2.0], b.getData())

    def test_add_shape(self):
        a = Tensor([1.0, 2.0, 3.0, 4.0], (2, 2))
        b = Tensor([5.0, 6.0, 7.0, 8.0], (2, 2))
        sum = a.add(b)
        self.assertEqual([6.0, 8.0, 10.0, 12.0], sum.getData())

    def test_add_broadcast(self):
        a = Tensor([1.0, 2.0], (1, 2))
        b = Tensor([3.0, 4.0], (2, 1))
        sum = a.add(b)
        self.assertEqual([4.0, 5.0, 5.0, 6.0], sum.getData())

    def test_subtract_shape(self):
        a = Tensor([1.0, 2.0, 3.0, 4.0], (2, 2))
        b = Tensor([5.0, 6.0, 7.0, 8.0], (2, 2))
        sum = b.subtract(a)
        self.assertEqual([4.0, 4.0, 4.0, 4.0], sum.getData())

    def test_subtract_broadcast(self):
        a = Tensor([5.0, 5.0], (2, 1))
        b = Tensor([1.0, 2.0], (1, 2))
        sum = a.subtract(b)
        self.assertEqual([4.0, 3.0, 4.0, 3.0], sum.getData())

    def test_hadamard_shape(self):
        a = Tensor([1.0, 2.0, 3.0, 4.0], (2, 2))
        b = Tensor([5.0, 6.0, 7.0, 8.0], (2, 2))
        sum = a.hadamardProduct(b)
        self.assertEqual([5.0, 12.0, 21.0, 32.0], sum.getData())

    def test_hadamard_broadcast(self):
        a = Tensor([1.0, 2.0], (1, 2))
        b = Tensor([3.0, 4.0], (2, 1))
        sum = a.hadamardProduct(b)
        self.assertEqual([3.0, 6.0, 4.0, 8.0], sum.getData())

    def test_multiply_2d(self):
        a = Tensor([1.0, 2.0, 3.0, 4.0], (2, 2))
        b = Tensor([5.0, 6.0, 7.0, 8.0], (2, 2))
        sum = a.multiply(b)
        self.assertEqual([19.0, 22.0, 43.0, 50.0], sum.getData())

    def test_multiply_3d(self):
        a = Tensor([[[1.0, 2.0], [3.0, 4.0]], [[9.0, 10.0], [11.0, 12.0]]])
        b = Tensor([[[5.0, 6.0], [7.0, 8.0]], [[13.0, 14.0], [15.0, 16.0]]])
        sum = a.multiply(b)
        self.assertEqual([19.0, 22.0, 43.0, 50.0, 267.0, 286.0, 323.0, 346.0], sum.getData())

if __name__ == '__main__':
    unittest.main()
