import unittest
from random import randrange

from Math.DiscreteDistribution import DiscreteDistribution


class DiscreteDistributionTest(unittest.TestCase):

    def setUp(self):
        self.smallDistribution = DiscreteDistribution()
        self.smallDistribution.addItem("item1")
        self.smallDistribution.addItem("item2")
        self.smallDistribution.addItem("item3")
        self.smallDistribution.addItem("item1")
        self.smallDistribution.addItem("item2")
        self.smallDistribution.addItem("item1")

    def test_AddItem1(self):
        self.assertEqual(3, self.smallDistribution.getCount("item1"))
        self.assertEqual(2, self.smallDistribution.getCount("item2"))
        self.assertEqual(1, self.smallDistribution.getCount("item3"))

    def test_AddItem2(self):
        discreteDistribution = DiscreteDistribution()
        for i in range(1000):
            discreteDistribution.addItem(randrange(1000).__str__())
        count = 0
        for i in range(1000):
            if discreteDistribution.containsItem(i.__str__()):
                count += discreteDistribution.getCount(i.__str__())
        self.assertEqual(1000, count)

    def test_AddItem3(self):
        discreteDistribution = DiscreteDistribution()
        for i in range(1000):
            discreteDistribution.addItem(randrange(1000).__str__())
        for i in range(1000000):
            discreteDistribution.addItem(randrange(1000000).__str__())
        self.assertAlmostEqual(len(discreteDistribution) / 1000000.0, 0.63212, 3)

    def test_RemoveItem(self):
        self.smallDistribution.removeItem("item1")
        self.smallDistribution.removeItem("item2")
        self.smallDistribution.removeItem("item3")
        self.assertEqual(2, self.smallDistribution.getCount("item1"))
        self.assertEqual(1, self.smallDistribution.getCount("item2"))
        self.smallDistribution.addItem("item1")
        self.smallDistribution.addItem("item2")
        self.smallDistribution.addItem("item3")

    def test_AddDistribution1(self):
        discreteDistribution = DiscreteDistribution()
        discreteDistribution.addItem("item4")
        discreteDistribution.addItem("item5")
        discreteDistribution.addItem("item5")
        discreteDistribution.addItem("item2")
        self.smallDistribution.addDistribution(discreteDistribution)
        self.assertEqual(3, self.smallDistribution.getCount("item1"))
        self.assertEqual(3, self.smallDistribution.getCount("item2"))
        self.assertEqual(1, self.smallDistribution.getCount("item3"))
        self.assertEqual(1, self.smallDistribution.getCount("item4"))
        self.assertEqual(2, self.smallDistribution.getCount("item5"))
        self.smallDistribution.removeDistribution(discreteDistribution)

    def test_AddDistribution2(self):
        discreteDistribution1 = DiscreteDistribution()
        for i in range(1000):
            discreteDistribution1.addItem(i.__str__())
        discreteDistribution2 = DiscreteDistribution()
        for i in range(500, 1000):
            discreteDistribution2.addItem((1000 + i).__str__())
        discreteDistribution1.addDistribution(discreteDistribution2)
        self.assertEqual(1500, len(discreteDistribution1))

    def test_RemoveDistribution(self):
        discreteDistribution = DiscreteDistribution()
        discreteDistribution.addItem("item1")
        discreteDistribution.addItem("item1")
        discreteDistribution.addItem("item2")
        self.smallDistribution.removeDistribution(discreteDistribution)
        self.assertEqual(1, self.smallDistribution.getCount("item1"))
        self.assertEqual(1, self.smallDistribution.getCount("item2"))
        self.assertEqual(1, self.smallDistribution.getCount("item3"))
        self.smallDistribution.addDistribution(discreteDistribution)

    def test_GetSum1(self):
        self.assertEqual(6, self.smallDistribution.getSum(), 0.0)

    def test_GetSum2(self):
        discreteDistribution = DiscreteDistribution()
        for i in range(1000):
            discreteDistribution.addItem(randrange(1000).__str__())
    
        self.assertEqual(1000, discreteDistribution.getSum(), 0.0)

    def test_GetIndex(self):
        self.assertEqual(0, self.smallDistribution.getIndex("item1"))
        self.assertEqual(1, self.smallDistribution.getIndex("item2"))
        self.assertEqual(2, self.smallDistribution.getIndex("item3"))

    def test_ContainsItem(self):
        self.assertTrue(self.smallDistribution.containsItem("item1"))
        self.assertFalse(self.smallDistribution.containsItem("item4"))

    def test_GetItem(self):
        self.assertEqual("item1", self.smallDistribution.getItem(0))
        self.assertEqual("item2", self.smallDistribution.getItem(1))
        self.assertEqual("item3", self.smallDistribution.getItem(2))

    def test_GetValue(self):
        self.assertEqual(3, self.smallDistribution.getValue(0))
        self.assertEqual(2, self.smallDistribution.getValue(1))
        self.assertEqual(1, self.smallDistribution.getValue(2))

    def test_GetCount(self):
        self.assertEqual(3, self.smallDistribution.getCount("item1"))
        self.assertEqual(2, self.smallDistribution.getCount("item2"))
        self.assertEqual(1, self.smallDistribution.getCount("item3"))

    def test_GetMaxItem1(self):
        self.assertEqual("item1", self.smallDistribution.getMaxItem())

    def test_GetMaxItem2(self):
        include = ["item2", "item3"]
        self.assertEqual("item2", self.smallDistribution.getMaxItemIncludeTheseOnly(include))

    def test_GetProbability1(self):
        discreteDistribution = DiscreteDistribution()
        for i in range(1000):
            discreteDistribution.addItem(i.__str__())
        self.assertEqual(0.001, discreteDistribution.getProbability(randrange(1000).__str__()))

    def test_GetProbability2(self):
        self.assertEqual(0.5, self.smallDistribution.getProbability("item1"))
        self.assertAlmostEqual(0.333333, self.smallDistribution.getProbability("item2"), 4)
        self.assertAlmostEqual(0.166667, self.smallDistribution.getProbability("item3"), 4)

    def test_GetProbabilityLaplaceSmoothing1(self):
        discreteDistribution = DiscreteDistribution()
        for i in range(1000):
            discreteDistribution.addItem(i.__str__())
        self.assertEqual(2.0 / 2001, discreteDistribution.getProbabilityLaplaceSmoothing(randrange(1000).__str__()))
        self.assertEqual(1.0 / 2001, discreteDistribution.getProbabilityLaplaceSmoothing("item0"))

    def test_getProbabilityLaplaceSmoothing2(self):
        self.assertEqual(0.4, self.smallDistribution.getProbabilityLaplaceSmoothing("item1"))
        self.assertEqual(0.3, self.smallDistribution.getProbabilityLaplaceSmoothing("item2"))
        self.assertEqual(0.2, self.smallDistribution.getProbabilityLaplaceSmoothing("item3"))
        self.assertEqual(0.1, self.smallDistribution.getProbabilityLaplaceSmoothing("item4"))

    def test_Entropy(self):
        self.assertAlmostEqual(1.4591, self.smallDistribution.entropy(), 4)


if __name__ == '__main__':
    unittest.main()
