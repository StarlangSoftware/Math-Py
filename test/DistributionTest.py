import unittest

from Math.Distribution import Distribution


class DistributionTest(unittest.TestCase):

    def test_ZNormal(self):
        self.assertAlmostEqual(0.5, Distribution.zNormal(0.0), 1)
        self.assertAlmostEqual(0.69146, Distribution.zNormal(0.5), 5)
        self.assertAlmostEqual(0.84134, Distribution.zNormal(1.0), 5)
        self.assertAlmostEqual(0.93319, Distribution.zNormal(1.5), 5)
        self.assertAlmostEqual(0.97725, Distribution.zNormal(2.0), 5)
        self.assertAlmostEqual(0.99379, Distribution.zNormal(2.5), 5)
        self.assertAlmostEqual(0.99865, Distribution.zNormal(3.0), 5)
        self.assertAlmostEqual(0.99977, Distribution.zNormal(3.5), 5)
        self.assertAlmostEqual(1 - Distribution.zNormal(0.5), Distribution.zNormal(-0.5), 5)
        self.assertAlmostEqual(1 - Distribution.zNormal(1.0), Distribution.zNormal(-1.0), 5)
        self.assertAlmostEqual(1 - Distribution.zNormal(1.5), Distribution.zNormal(-1.5), 5)
        self.assertAlmostEqual(1 - Distribution.zNormal(2.0), Distribution.zNormal(-2.0), 5)
        self.assertAlmostEqual(1 - Distribution.zNormal(2.5), Distribution.zNormal(-2.5), 5)
        self.assertAlmostEqual(1 - Distribution.zNormal(3.0), Distribution.zNormal(-3.0), 5)
        self.assertAlmostEqual(1 - Distribution.zNormal(3.5), Distribution.zNormal(-3.5), 5)

    def test_ZInverse(self):
        self.assertAlmostEqual(0.0, Distribution.zInverse(0.5), 5)
        self.assertAlmostEqual(0.841621, Distribution.zInverse(0.8), 5)
        self.assertAlmostEqual(1.281552, Distribution.zInverse(0.9), 5)
        self.assertAlmostEqual(1.644854, Distribution.zInverse(0.95), 5)
        self.assertAlmostEqual(2.053749, Distribution.zInverse(0.98), 5)
        self.assertAlmostEqual(2.326348, Distribution.zInverse(0.99), 5)
        self.assertAlmostEqual(2.575829, Distribution.zInverse(0.995), 5)
        self.assertAlmostEqual(2.878162, Distribution.zInverse(0.998), 5)
        self.assertAlmostEqual(3.090232, Distribution.zInverse(0.999), 5)

    def test_ChiSquare(self):
        self.assertAlmostEqual(0.05, Distribution.chiSquare(3.841, 1), 4)
        self.assertAlmostEqual(0.005, Distribution.chiSquare(7.879, 1), 4)
        self.assertAlmostEqual(0.95, Distribution.chiSquare(3.940, 10), 4)
        self.assertAlmostEqual(0.05, Distribution.chiSquare(18.307, 10), 4)
        self.assertAlmostEqual(0.995, Distribution.chiSquare(2.156, 10), 4)
        self.assertAlmostEqual(0.005, Distribution.chiSquare(25.188, 10), 4)
        self.assertAlmostEqual(0.95, Distribution.chiSquare(77.929, 100), 4)
        self.assertAlmostEqual(0.05, Distribution.chiSquare(124.342, 100), 4)
        self.assertAlmostEqual(0.995, Distribution.chiSquare(67.328, 100), 4)
        self.assertAlmostEqual(0.005, Distribution.chiSquare(140.169, 100), 4)

    def test_ChiSquareInverse(self):
        self.assertAlmostEqual(2.706, Distribution.chiSquareInverse(0.1, 1), 3)
        self.assertAlmostEqual(6.635, Distribution.chiSquareInverse(0.01, 1), 3)
        self.assertAlmostEqual(4.865, Distribution.chiSquareInverse(0.9, 10), 3)
        self.assertAlmostEqual(15.987, Distribution.chiSquareInverse(0.1, 10), 3)
        self.assertAlmostEqual(2.558, Distribution.chiSquareInverse(0.99, 10), 3)
        self.assertAlmostEqual(23.209, Distribution.chiSquareInverse(0.01, 10), 3)
        self.assertAlmostEqual(82.358, Distribution.chiSquareInverse(0.9, 100), 3)
        self.assertAlmostEqual(118.498, Distribution.chiSquareInverse(0.1, 100), 3)
        self.assertAlmostEqual(70.065, Distribution.chiSquareInverse(0.99, 100), 3)
        self.assertAlmostEqual(135.807, Distribution.chiSquareInverse(0.01, 100), 3)

    def test_FDistribution(self):
        self.assertAlmostEqual(0.1, Distribution.fDistribution(39.86346, 1, 1), 5)
        self.assertAlmostEqual(0.1, Distribution.fDistribution(2.32260, 10, 10), 5)
        self.assertAlmostEqual(0.1, Distribution.fDistribution(1.79384, 20, 20), 5)
        self.assertAlmostEqual(0.1, Distribution.fDistribution(1.60648, 30, 30), 5)
        self.assertAlmostEqual(0.05, Distribution.fDistribution(161.4476, 1, 1), 5)
        self.assertAlmostEqual(0.05, Distribution.fDistribution(2.9782, 10, 10), 5)
        self.assertAlmostEqual(0.05, Distribution.fDistribution(2.1242, 20, 20), 5)
        self.assertAlmostEqual(0.05, Distribution.fDistribution(1.8409, 30, 30), 5)
        self.assertAlmostEqual(0.01, Distribution.fDistribution(4052.181, 1, 1), 5)
        self.assertAlmostEqual(0.01, Distribution.fDistribution(4.849, 10, 10), 5)
        self.assertAlmostEqual(0.01, Distribution.fDistribution(2.938, 20, 20), 5)
        self.assertAlmostEqual(0.01, Distribution.fDistribution(2.386, 30, 30), 5)

    def test_FDistributionInverse(self):
        self.assertAlmostEqual(3.818, Distribution.fDistributionInverse(0.01, 5, 26), 3)
        self.assertAlmostEqual(15.1010, Distribution.fDistributionInverse(0.025, 4, 3), 3)
        self.assertAlmostEqual(2.19535, Distribution.fDistributionInverse(0.1, 8, 13), 3)
        self.assertAlmostEqual(2.29871, Distribution.fDistributionInverse(0.1, 3, 27), 3)
        self.assertAlmostEqual(3.4381, Distribution.fDistributionInverse(0.05, 8, 8), 3)
        self.assertAlmostEqual(2.6283, Distribution.fDistributionInverse(0.05, 6, 19), 3)
        self.assertAlmostEqual(3.3120, Distribution.fDistributionInverse(0.025, 9, 13), 3)
        self.assertAlmostEqual(3.7505, Distribution.fDistributionInverse(0.025, 3, 23), 3)
        self.assertAlmostEqual(4.155, Distribution.fDistributionInverse(0.01, 12, 12), 3)
        self.assertAlmostEqual(6.851, Distribution.fDistributionInverse(0.01, 1, 120), 3)

    def test_TDistribution(self):
        self.assertAlmostEqual(0.05, Distribution.tDistribution(6.314, 1), 4)
        self.assertAlmostEqual(0.005, Distribution.tDistribution(63.656, 1), 4)
        self.assertAlmostEqual(0.05, Distribution.tDistribution(1.812, 10), 4)
        self.assertAlmostEqual(0.01, Distribution.tDistribution(2.764, 10), 4)
        self.assertAlmostEqual(0.005, Distribution.tDistribution(3.169, 10), 4)
        self.assertAlmostEqual(0.001, Distribution.tDistribution(4.144, 10), 4)
        self.assertAlmostEqual(0.05, Distribution.tDistribution(1.725, 20), 4)
        self.assertAlmostEqual(0.01, Distribution.tDistribution(2.528, 20), 4)
        self.assertAlmostEqual(0.005, Distribution.tDistribution(2.845, 20), 4)
        self.assertAlmostEqual(0.001, Distribution.tDistribution(3.552, 20), 4)

    def test_TDistributionInverse(self):
        self.assertAlmostEqual(2.947, Distribution.tDistributionInverse(0.005, 15), 3)
        self.assertAlmostEqual(1.717, Distribution.tDistributionInverse(0.05, 22), 3)
        self.assertAlmostEqual(3.365, Distribution.tDistributionInverse(0.01, 5), 3)
        self.assertAlmostEqual(3.922, Distribution.tDistributionInverse(0.0005, 18), 3)
        self.assertAlmostEqual(3.467, Distribution.tDistributionInverse(0.001, 24), 3)
        self.assertAlmostEqual(6.314, Distribution.tDistributionInverse(0.05, 1), 3)
        self.assertAlmostEqual(2.306, Distribution.tDistributionInverse(0.025, 8), 3)
        self.assertAlmostEqual(3.646, Distribution.tDistributionInverse(0.001, 17), 3)
        self.assertAlmostEqual(3.373, Distribution.tDistributionInverse(0.0005, 120), 3)


if __name__ == '__main__':
    unittest.main()
