import unittest
import math

from Math.Vector import Vector


class VectorTest(unittest.TestCase):
    data1 = [2, 3, 4, 5, 6]

    def setUp(self):
        data2 = [8, 7, 6, 5, 4]
        self.smallVector1 = Vector(self.data1)
        self.smallVector2 = Vector(data2)
        largeData1 = []
        for i in range(1, 1001):
            largeData1.append(i)
        self.largeVector1 = Vector(largeData1)
        largeData2 = []
        for i in range(1, 1001):
            largeData2.append(1000 - i + 1)
        self.largeVector2 = Vector(largeData2)

    def test_Biased(self):
        biased = self.smallVector1.biased()
        self.assertEqual(1, biased.getValue(0))
        self.assertEqual(self.smallVector1.size() + 1, biased.size())

    def test_ElementAdd(self):
        self.smallVector1.add(7)
        self.assertEqual(7, self.smallVector1.getValue(5))
        self.assertEqual(6, self.smallVector1.size())
        self.smallVector1.remove(5)

    def test_Insert(self):
        self.smallVector1.insert(3, 6)
        self.assertEqual(6, self.smallVector1.getValue(3))
        self.assertEqual(6, self.smallVector1.size())
        self.smallVector1.remove(3)

    def test_Remove(self):
        self.smallVector1.remove(2)
        self.assertEqual(5, self.smallVector1.getValue(2))
        self.assertEqual(4, self.smallVector1.size())
        self.smallVector1.insert(2, 4)

    def test_SumOfElementsSmall(self):
        self.assertEqual(20, self.smallVector1.sumOfElements())
        self.assertEqual(30, self.smallVector2.sumOfElements())

    def test_SumOfElementsLarge(self):
        self.assertEqual(20, self.smallVector1.sumOfElements())
        self.assertEqual(30, self.smallVector2.sumOfElements())
        self.assertEqual(500500, self.largeVector1.sumOfElements())
        self.assertEqual(500500, self.largeVector2.sumOfElements())

    def test_MaxIndex(self):
        self.assertEqual(4, self.smallVector1.maxIndex())
        self.assertEqual(0, self.smallVector2.maxIndex())

    def test_Sigmoid(self):
        smallVector3 = Vector(self.data1)
        smallVector3.sigmoid()
        self.assertAlmostEqual(0.8807971, smallVector3.getValue(0), 6)
        self.assertAlmostEqual(0.9975274, smallVector3.getValue(4), 6)

    def test_SkipVectorSmall(self):
        smallVector3 = self.smallVector1.skipVector(2, 0)
        self.assertEqual(2, smallVector3.getValue(0))
        self.assertEqual(6, smallVector3.getValue(2))
        smallVector3 = self.smallVector1.skipVector(3, 1)
        self.assertEqual(3, smallVector3.getValue(0))
        self.assertEqual(6, smallVector3.getValue(1))

    def test_SkipVectorLarge(self):
        largeVector3 = self.largeVector1.skipVector(2, 0)
        self.assertEqual(250000, largeVector3.sumOfElements())
        largeVector3 = self.largeVector1.skipVector(5, 3)
        self.assertEqual(100300, largeVector3.sumOfElements())

    def test_VectorAddSmall(self):
        self.smallVector1.addVector(self.smallVector2)
        self.assertEqual(50, self.smallVector1.sumOfElements())
        self.smallVector1.subtract(self.smallVector2)

    def test_VectorAddLarge(self):
        self.largeVector1.addVector(self.largeVector2)
        self.assertEqual(1001000, self.largeVector1.sumOfElements())
        self.largeVector1.subtract(self.largeVector2)

    def test_SubtractSmall(self):
        self.smallVector1.subtract(self.smallVector2)
        self.assertEqual(-10, self.smallVector1.sumOfElements())
        self.smallVector1.addVector(self.smallVector2)

    def test_SubtractLarge(self):
        self.largeVector1.subtract(self.largeVector2)
        self.assertEqual(0, self.largeVector1.sumOfElements())
        self.largeVector1.addVector(self.largeVector2)

    def test_DifferenceSmall(self):
        smallVector3 = self.smallVector1.difference(self.smallVector2)
        self.assertEqual(-10, smallVector3.sumOfElements())

    def test_DifferenceLarge(self):
        largeVector3 = self.largeVector1.difference(self.largeVector2)
        self.assertEqual(0, largeVector3.sumOfElements())

    def test_DotProductWithVectorSmall(self):
        dotProduct = self.smallVector1.dotProduct(self.smallVector2)
        self.assertEqual(110, dotProduct)

    def test_DotProductWithVectorLarge(self):
        dotProduct = self.largeVector1.dotProduct(self.largeVector2)
        self.assertEqual(167167000, dotProduct)

    def test_DotProductWithItselfSmall(self):
        dotProduct = self.smallVector1.dotProductWithSelf()
        self.assertEqual(90, dotProduct)

    def test_DotProductWithItselfLarge(self):
        dotProduct = self.largeVector1.dotProductWithSelf()
        self.assertEqual(333833500, dotProduct)

    def test_ElementProductSmall(self):
        smallVector3 = self.smallVector1.elementProduct(self.smallVector2)
        self.assertEqual(110, smallVector3.sumOfElements())

    def test_ElementProductLarge(self):
        largeVector3 = self.largeVector1.elementProduct(self.largeVector2)
        self.assertEqual(167167000, largeVector3.sumOfElements())

    def test_Divide(self):
        self.smallVector1.divide(10.0)
        self.assertEqual(2, self.smallVector1.sumOfElements())
        self.smallVector1.multiply(10.0)

    def test_Multiply(self):
        self.smallVector1.multiply(10.0)
        self.assertEqual(200, self.smallVector1.sumOfElements())
        self.smallVector1.divide(10.0)

    def test_Product(self):
        smallVector3 = self.smallVector1.product(7.0)
        self.assertEqual(140, smallVector3.sumOfElements())

    def test_L1NormalizeSmall(self):
        self.smallVector1.l1Normalize()
        self.assertEqual(1.0, self.smallVector1.sumOfElements())
        self.smallVector1.multiply(20)

    def test_L1NormalizeLarge(self):
        self.largeVector1.l1Normalize()
        self.assertEqual(1.0, self.largeVector1.sumOfElements())
        self.largeVector1.multiply(500500)

    def test_L2NormSmall(self):
        norm = self.smallVector1.l2Norm()
        self.assertEqual(norm, math.sqrt(90))

    def test_L2NormLarge(self):
        norm = self.largeVector1.l2Norm()
        self.assertEqual(norm, math.sqrt(333833500))

    def test_cosineSimilaritySmall(self):
        similarity = self.smallVector1.cosineSimilarity(self.smallVector2)
        self.assertAlmostEqual(0.8411910, similarity, 6)

    def test_cosineSimilarityLarge(self):
        similarity = self.largeVector1.cosineSimilarity(self.largeVector2)
        self.assertAlmostEqual(0.5007497, similarity, 6)


if __name__ == '__main__':
    unittest.main()
