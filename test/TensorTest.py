import unittest
from Math.Tensor import Tensor

class TensorTest(unittest.TestCase):
    def test_constructor_with_inferred_shape(self):
        data = [[1.0, 2.0], [3.0, 4.0]]
        tensor = Tensor(data)
        self.assertEqual(tensor.shape, (2, 2))
        self.assertEqual(tensor.data, [1.0, 2.0, 3.0, 4.0])

    def test_constructor_with_explicit_shape(self):
        data = [1.0, 2.0, 3.0, 4.0]
        tensor = Tensor(data, (2, 2))
        self.assertEqual(tensor.shape, (2, 2))
        self.assertEqual(tensor.data, [1.0, 2.0, 3.0, 4.0])

    def test_constructor_shape_mismatch(self):
        data = [1.0, 2.0, 3.0]
        with self.assertRaises(ValueError) as cm:
            Tensor(data, (2, 2))
        self.assertIn("Shape does not match the number of elements in data.", str(cm.exception))

    def test_get_shape(self):
        data = [1.0, 2.0, 3.0]
        tensor = Tensor(data, (3,))
        self.assertEqual(tensor.shape, (3,))

    def test_get_data(self):
        data = [1.0, 2.0, 3.0, 4.0]
        tensor = Tensor(data, (2, 2))
        self.assertEqual(tensor.data, data)

    def test_get_valid_indices(self):
        data = [1.0, 2.0, 3.0, 4.0]
        tensor = Tensor(data, (2, 2))
        self.assertAlmostEqual(tensor.get((0, 0)), 1.0, places=9)
        self.assertAlmostEqual(tensor.get((1, 1)), 4.0, places=9)

    def test_get_out_of_bounds_indices(self):
        data = [1.0, 2.0]
        tensor = Tensor(data, (2,))
        with self.assertRaises(IndexError):
            tensor.get((2,))

    def test_set_valid_indices(self):
        data = [1.0, 2.0, 3.0, 4.0]
        tensor = Tensor(data, (2, 2))
        tensor.set((0, 0), 5.0)
        self.assertAlmostEqual(tensor.get((0, 0)), 5.0, places=9)

    def test_set_out_of_bounds_indices(self):
        data = [1.0, 2.0]
        tensor = Tensor(data, (2,))
        with self.assertRaises(IndexError):
            tensor.set((2,), 5.0)

    def test_reshape_valid(self):
        data = [1.0, 2.0, 3.0, 4.0]
        tensor = Tensor(data, (2, 2))
        reshaped = tensor.reshape((4,))
        self.assertEqual(reshaped.shape, (4,))
        self.assertEqual(reshaped.data, data)

    def test_reshape_invalid(self):
        data = [1.0, 2.0, 3.0]
        tensor = Tensor(data, (3,))
        with self.assertRaises(ValueError) as cm:
            tensor.reshape((2, 2))
        self.assertIn("Total number of elements must remain the same.", str(cm.exception))

    def test_transpose_no_axes(self):
        data = [[1.0, 2.0], [3.0, 4.0]]
        tensor = Tensor(data)
        transposed = tensor.transpose()
        self.assertEqual(transposed.shape, (2, 2))
        self.assertEqual(transposed.data, [1.0, 3.0, 2.0, 4.0])

    def test_transpose_with_axes(self):
        data = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]
        tensor = Tensor(data)
        transposed = tensor.transpose((1, 0))
        self.assertEqual(transposed.shape, (3, 2))
        self.assertEqual(transposed.data, [1.0, 4.0, 2.0, 5.0, 3.0, 6.0])

    def test_transpose_invalid_axes_length(self):
        data = [[1.0, 2.0], [3.0, 4.0]]
        tensor = Tensor(data)
        with self.assertRaises(ValueError) as cm:
            tensor.transpose((0,))
        self.assertIn("Invalid transpose axes.", str(cm.exception))

    def test_transpose_invalid_axes_value(self):
        data = [[1.0, 2.0], [3.0, 4.0]]
        tensor = Tensor(data)
        with self.assertRaises(ValueError) as cm:
            tensor.transpose((0, 2))
        self.assertIn("Invalid transpose axes.", str(cm.exception))

    def test_broadcast_to_valid(self):
        data = [1.0, 2.0]
        tensor = Tensor(data, (1, 2))
        broadcasted = tensor.broadcast_to((2, 2))
        self.assertEqual(broadcasted.shape, (2, 2))
        self.assertEqual(broadcasted.data, [1.0, 2.0, 1.0, 2.0])

    def test_broadcast_to_invalid(self):
        data = [1.0, 2.0]
        tensor = Tensor(data, (2,))
        with self.assertRaises(ValueError) as cm:
            tensor.broadcast_to((3,))
        self.assertIn("Cannot broadcast shape", str(cm.exception))

    def test_add_same_shape(self):
        data1 = [1.0, 2.0, 3.0, 4.0]
        tensor1 = Tensor(data1, (2, 2))
        data2 = [5.0, 6.0, 7.0, 8.0]
        tensor2 = Tensor(data2, (2, 2))
        sum_tensor = tensor1.add(tensor2)
        self.assertEqual(sum_tensor.shape, (2, 2))
        self.assertEqual(sum_tensor.data, [6.0, 8.0, 10.0, 12.0])

    def test_add_with_broadcasting(self):
        data1 = [1.0, 2.0]
        tensor1 = Tensor(data1, (1, 2))
        data2 = [3.0, 4.0]
        tensor2 = Tensor(data2, (2, 1))
        sum_tensor = tensor1.add(tensor2)
        self.assertEqual(sum_tensor.shape, (2, 2))
        self.assertEqual(sum_tensor.data, [4.0, 5.0, 5.0, 6.0])

    def test_subtract_same_shape(self):
        data1 = [5.0, 6.0, 7.0, 8.0]
        tensor1 = Tensor(data1, (2, 2))
        data2 = [1.0, 2.0, 3.0, 4.0]
        tensor2 = Tensor(data2, (2, 2))
        diff = tensor1.subtract(tensor2)
        self.assertEqual(diff.shape, (2, 2))
        self.assertEqual(diff.data, [4.0, 4.0, 4.0, 4.0])

    def test_subtract_with_broadcasting(self):
        data1 = [5.0, 5.0]
        tensor1 = Tensor(data1, (2, 1))
        data2 = [1.0, 2.0]
        tensor2 = Tensor(data2, (1, 2))
        diff = tensor1.subtract(tensor2)
        self.assertEqual(diff.shape, (2, 2))
        self.assertEqual(diff.data, [4.0, 3.0, 4.0, 3.0])

    def test_hadamard_product_same_shape(self):
        data1 = [1.0, 2.0, 3.0, 4.0]
        tensor1 = Tensor(data1, (2, 2))
        data2 = [5.0, 6.0, 7.0, 8.0]
        tensor2 = Tensor(data2, (2, 2))
        product = tensor1.hadamardProduct(tensor2)
        self.assertEqual(product.shape, (2, 2))
        self.assertEqual(product.data, [5.0, 12.0, 21.0, 32.0])

    def test_hadamard_product_with_broadcasting(self):
        data1 = [1.0, 2.0]
        tensor1 = Tensor(data1, (1, 2))
        data2 = [3.0, 4.0]
        tensor2 = Tensor(data2, (2, 1))
        product = tensor1.hadamardProduct(tensor2)
        self.assertEqual(product.shape, (2, 2))
        self.assertEqual(product.data, [3.0, 6.0, 4.0, 8.0])

    def test_matrix_multiply_2d(self):
        data1 = [[1.0, 2.0], [3.0, 4.0]]
        data2 = [[5.0, 6.0], [7.0, 8.0]]
        tensor1 = Tensor(data1)
        tensor2 = Tensor(data2)
        result = tensor1.multiply(tensor2)
        self.assertEqual(result.shape, (2, 2))
        self.assertEqual(result.data, [19.0, 22.0, 43.0, 50.0])

    def test_matrix_multiply_3d(self):
        data1 = [
            [[1.0, 2.0], [3.0, 4.0]],
            [[9.0, 10.0], [11.0, 12.0]]
        ]
        data2 = [
            [[5.0, 6.0], [7.0, 8.0]],
            [[13.0, 14.0], [15.0, 16.0]]
        ]
        tensor1 = Tensor(data1)
        tensor2 = Tensor(data2)
        result = tensor1.multiply(tensor2)
        self.assertEqual(result.shape, (2, 2, 2))
        self.assertEqual(result.data, [19.0, 22.0, 43.0, 50.0, 267.0, 286.0, 323.0, 346.0])

    def test_matrix_multiply_invalid_shapes(self):
        data1 = [1.0, 2.0, 3.0]
        tensor1 = Tensor(data1, (3,))
        data2 = [[4.0, 5.0], [6.0, 7.0]]
        tensor2 = Tensor(data2)
        with self.assertRaises(ValueError) as cm:
            tensor1.multiply(tensor2)
        self.assertIn("Shapes", str(cm.exception))

    def test_matrix_multiply_unsupported_dimensions(self):
        # Test with incompatible 2D shapes
        data1 = [1.0, 2.0, 3.0, 4.0]
        tensor1 = Tensor(data1, (2, 2))
        data2 = [5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
        tensor2 = Tensor(data2, (3, 2))  # Incompatible: (2,2) * (3,2) - inner dimensions don't match
        with self.assertRaises(ValueError) as cm:
            tensor1.multiply(tensor2)
        self.assertIn("Shapes", str(cm.exception))

    def test_partial_valid(self):
        data = [
            [1.0, 2.0, 3.0],
            [4.0, 5.0, 6.0],
            [7.0, 8.0, 9.0]
        ]
        tensor = Tensor(data)
        partial = tensor.partial((0, 1), (2, 3))
        self.assertEqual(partial.shape, (2, 2))
        self.assertEqual(partial.data, [2.0, 3.0, 5.0, 6.0])

    def test_partial_invalid_indices_length(self):
        data = [[1.0, 2.0], [3.0, 4.0]]
        tensor = Tensor(data)
        with self.assertRaises(ValueError) as cm:
            tensor.partial((0,), (1,))
        self.assertIn("start_indices and end_indices must match the number of dimensions.", str(cm.exception))

    def test_partial_invalid_indices_range(self):
        data = [[1.0, 2.0], [3.0, 4.0]]
        tensor = Tensor(data)
        with self.assertRaises(IndexError):
            tensor.partial((0, 0), (3, 1))

    def test_to_string_method(self):
        data = [[1.0, 2.0], [3.0, 4.0]]
        tensor = Tensor(data)
        self.assertEqual(repr(tensor), "Tensor(shape=(2, 2), data=[[1.0, 2.0], [3.0, 4.0]])")

    def test_print_demo(self):
        # 1D Vectors
        v1 = Tensor([1.0, 2.0, 3.0], (3,))
        v2 = Tensor([4.0, 5.0, 6.0], (3,))
        hadamard_vec = v1.hadamardProduct(v2)
        # 2D Matrices
        a = Tensor([1.0, 2.0, 3.0, 4.0], (2, 2))
        b = Tensor([5.0, 6.0, 7.0, 8.0], (2, 2))
        hadamard_mat = a.hadamardProduct(b)
        matrix_mul = a.multiply(b)
        # 3D Batch Matrices
        data1 = [
            [[1.0, 2.0], [3.0, 4.0]],
            [[9.0, 10.0], [11.0, 12.0]]
        ]
        data2 = [
            [[5.0, 6.0], [7.0, 8.0]],
            [[13.0, 14.0], [15.0, 16.0]]
        ]
        batchA = Tensor(data1)
        batchB = Tensor(data2)
        batch_matrix_mul = batchA.multiply(batchB)
        # Just check that no exceptions are raised and outputs are as expected
        self.assertEqual(hadamard_vec.data, [4.0, 10.0, 18.0])
        self.assertEqual(hadamard_mat.data, [5.0, 12.0, 21.0, 32.0])
        self.assertEqual(matrix_mul.data, [19.0, 22.0, 43.0, 50.0])
        self.assertEqual(batch_matrix_mul.data, [19.0, 22.0, 43.0, 50.0, 267.0, 286.0, 323.0, 346.0])

if __name__ == "__main__":
    unittest.main()
