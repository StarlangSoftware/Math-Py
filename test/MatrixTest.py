import unittest
from random import randrange

from Math.Matrix import Matrix
from Math.Vector import Vector


class MatrixTest(unittest.TestCase):

    def setUp(self):
        self.small = Matrix(3, 3)
        for i in range(3):
            for j in range(3):
                self.small.setValue(i, j, 1.0)
        self.v = Vector(3, 1.0)
        self.large = Matrix(1000, 1000)
        for i in range(1000):
            for j in range(1000):
                self.large.setValue(i, j, 1.0)
        self.medium = Matrix(100, 100)
        for i in range(100):
            for j in range(100):
                self.medium.setValue(i, j, 1.0)
        self.V = Vector(1000, 1.0)
        self.vr = Vector(100, 1.0)
        self.random = Matrix(100, 100, 1, 10, 1)
        self.originalSum = self.random.sumOfElements()
        self.identity = Matrix(100)

    def test_ColumnWiseNormalize(self):
        mClone = self.small.clone()
        mClone.columnWiseNormalize()
        self.assertEqual(3, mClone.sumOfElements())
        MClone = self.large.clone()
        MClone.columnWiseNormalize()
        self.assertAlmostEqual(1000, MClone.sumOfElements(), 3)
        self.identity.columnWiseNormalize()
        self.assertEqual(100, self.identity.sumOfElements())

    def test_MultiplyWithConstant(self):
        self.small.multiplyWithConstant(4)
        self.assertEqual(36, self.small.sumOfElements())
        self.small.divideByConstant(4)
        self.large.multiplyWithConstant(1.001)
        self.assertAlmostEqual(1001000, self.large.sumOfElements(), 3)
        self.large.divideByConstant(1.001)
        self.random.multiplyWithConstant(3.6)
        self.assertAlmostEqual(self.originalSum * 3.6, self.random.sumOfElements(), 4)
        self.random.divideByConstant(3.6)

    def test_DivideByConstant(self):
        self.small.divideByConstant(4)
        self.assertEqual(2.25, self.small.sumOfElements())
        self.small.multiplyWithConstant(4)
        self.large.divideByConstant(10)
        self.assertAlmostEqual(100000, self.large.sumOfElements(), 3)
        self.large.multiplyWithConstant(10)
        self.random.divideByConstant(3.6)
        self.assertAlmostEqual(self.originalSum / 3.6, self.random.sumOfElements(), 4)
        self.random.multiplyWithConstant(3.6)

    def test_Add(self):
        self.random.add(self.identity)
        self.assertAlmostEqual(self.originalSum + 100, self.random.sumOfElements(), 4)
        self.random.subtract(self.identity)

    def test_AddVector(self):
        self.large.addRowVector(4, self.V)
        self.assertEqual(1001000, self.large.sumOfElements(), 0.0)
        self.V.multiply(-1.0)
        self.large.addRowVector(4, self.V)
        self.V.multiply(-1.0)

    def test_Subtract(self):
        self.random.subtract(self.identity)
        self.assertAlmostEqual(self.originalSum - 100, self.random.sumOfElements(), 4)
        self.random.add(self.identity)

    def test_MultiplyWithVectorFromLeft(self):
        result = self.small.multiplyWithVectorFromLeft(self.v)
        self.assertEqual(9, result.sumOfElements())
        result = self.large.multiplyWithVectorFromLeft(self.V)
        self.assertEqual(1000000, result.sumOfElements())
        result = self.random.multiplyWithVectorFromLeft(self.vr)
        self.assertAlmostEqual(self.originalSum, result.sumOfElements(), 4)

    def test_MultiplyWithVectorFromRight(self):
        result = self.small.multiplyWithVectorFromRight(self.v)
        self.assertEqual(9, result.sumOfElements())
        result = self.large.multiplyWithVectorFromRight(self.V)
        self.assertEqual(1000000, result.sumOfElements())
        result = self.random.multiplyWithVectorFromRight(self.vr)
        self.assertAlmostEqual(self.originalSum, result.sumOfElements(), 4)

    def test_ColumnSum(self):
        self.assertEqual(3, self.small.columnSum(randrange(3)))
        self.assertEqual(1000, self.large.columnSum(randrange(1000)))
        self.assertEqual(1, self.identity.columnSum(randrange(100)))

    def test_SumOfRows(self):
        self.assertEqual(9, self.small.sumOfRows().sumOfElements())
        self.assertEqual(1000000, self.large.sumOfRows().sumOfElements())
        self.assertEqual(100, self.identity.sumOfRows().sumOfElements())
        self.assertAlmostEqual(self.originalSum, self.random.sumOfRows().sumOfElements(), 3)

    def test_RowSum(self):
        self.assertEqual(3, self.small.rowSum(randrange(3)))
        self.assertEqual(1000, self.large.rowSum(randrange(1000)))
        self.assertEqual(1, self.identity.rowSum(randrange(100)))

    def test_Multiply(self):
        result = self.small.multiply(self.small)
        self.assertEqual(27, result.sumOfElements())
        result = self.medium.multiply(self.medium)
        self.assertEqual(1000000.0, result.sumOfElements())
        result = self.random.multiply(self.identity)
        self.assertEqual(self.originalSum, result.sumOfElements())
        result = self.identity.multiply(self.random)
        self.assertEqual(self.originalSum, result.sumOfElements())

    def test_ElementProduct(self):
        result = self.small.elementProduct(self.small)
        self.assertEqual(9, result.sumOfElements())
        result = self.large.elementProduct(self.large)
        self.assertEqual(1000000, result.sumOfElements())
        result = self.random.elementProduct(self.identity)
        self.assertEqual(result.trace(), result.sumOfElements())

    def test_SumOfElements(self):
        self.assertEqual(9, self.small.sumOfElements())
        self.assertEqual(1000000, self.large.sumOfElements())
        self.assertEqual(100, self.identity.sumOfElements())
        self.assertEqual(self.originalSum, self.random.sumOfElements())

    def test_Trace(self):
        self.assertEqual(3, self.small.trace())
        self.assertEqual(1000, self.large.trace())
        self.assertEqual(100, self.identity.trace())

    def test_Transpose(self):
        self.assertEqual(9, self.small.transpose().sumOfElements())
        self.assertEqual(1000000, self.large.transpose().sumOfElements())
        self.assertEqual(100, self.identity.transpose().sumOfElements())
        self.assertAlmostEqual(self.originalSum, self.random.transpose().sumOfElements(), 3)

    def test_IsSymmetric(self):
        self.assertTrue(self.small.isSymmetric())
        self.assertTrue(self.large.isSymmetric())
        self.assertTrue(self.identity.isSymmetric())
        self.assertFalse(self.random.isSymmetric())

    def test_Determinant(self):
        self.assertEqual(0, self.small.determinant())
        self.assertEqual(0, self.large.determinant())
        self.assertEqual(1, self.identity.determinant())

    def test_Inverse(self):
        self.identity.inverse()
        self.assertEqual(100, self.identity.sumOfElements())
        self.random.inverse()
        self.random.inverse()
        self.assertAlmostEqual(self.originalSum, self.random.sumOfElements(), 5)

    def test_Characteristics(self):
        vectors = self.small.characteristics()
        self.assertEqual(2, len(vectors))
        vectors = self.identity.characteristics()
        self.assertEqual(100, len(vectors))
        vectors = self.medium.characteristics()
        self.assertEqual(46, len(vectors))


if __name__ == '__main__':
    unittest.main()
