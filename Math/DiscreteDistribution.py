from __future__ import annotations
import collections
import math


class DiscreteDistribution(collections.OrderedDict):

    __sum: float

    def __init__(self, **kwargs):
        """
        A constructor of DiscreteDistribution class which calls its super class.
        """
        super().__init__(**kwargs)
        self.__sum = 0.0

    def addItem(self, item: str):
        """
        The addItem method takes a String item as an input and if this map contains a mapping for the item it puts the
        item with given value + 1, else it puts item with value of 1.

        PARAMETERS
        ----------
        item : string
            String input.
        """
        if item in self:
            self[item] = self[item] + 1
        else:
            self[item] = 1
        self.__sum = self.__sum + 1

    def removeItem(self, item: str):
        """
        The removeItem method takes a String item as an input and if this map contains a mapping for the item it puts
        the item with given value - 1, and if its value is 0, it removes the item.

        PARAMETERS
        ----------
        item : string
            String input.
        """
        if item in self:
            self[item] = self[item] - 1
            if self[item] == 0:
                self.pop(item)

    def addDistribution(self, distribution: DiscreteDistribution):
        """
        The addDistribution method takes a DiscreteDistribution as an input and loops through the entries in this
        distribution and if this map contains a mapping for the entry it puts the entry with its value + entry,
        else it puts entry with its value. It also accumulates the values of entries and assigns to the sum variable.

        PARAMETERS
        ----------
        distribution : DiscreteDistribution
            DiscreteDistribution type input.
        """
        for entry in distribution:
            if entry in self:
                self[entry] = self[entry] + distribution[entry]
            else:
                self[entry] = distribution[entry]
            self.__sum += distribution[entry]

    def removeDistribution(self, distribution: DiscreteDistribution):
        """
        The removeDistribution method takes a DiscreteDistribution as an input and loops through the entries in this
        distribution and if this map contains a mapping for the entry it puts the entry with its key - value, else it
        removes the entry. It also decrements the value of entry from sum and assigns to the sum variable.

        PARAMETERS
        ----------
        distribution : DiscreteDistribution
            DiscreteDistribution type input.
        """
        for entry in distribution:
            if self[entry] - distribution[entry] != 0:
                self[entry] -= distribution[entry]
            else:
                self.pop(entry)
            self.__sum -= distribution[entry]

    def getSum(self) -> float:
        """
        The getter for sum variable.

        RETURNS
        -------
        double
            sum
        """
        return self.__sum

    def getIndex(self, item: str) -> int:
        """
        The getIndex method takes an item as an input and returns the index of given item.

        PARAMETERS
        ----------
        item : string
            item to search for index.

        RETURNS
        -------
        int
            index of given item.
        """
        return list(self.keys()).index(item)

    def containsItem(self, item: str) -> bool:
        """
        The containsItem method takes an item as an input and returns true if this map contains a mapping for the
        given item.

        PARAMETERS
        ----------
        item : string
            item to check.

        RETURNS
        -------
        boolean
            true if this map contains a mapping for the given item.
        """
        return item in self

    def getItem(self, index: int) -> str:
        """
        The getItem method takes an index as an input and returns the item at given index.

        PARAMETERS
        ----------
        index : int
            index is used for searching the item.

        RETURNS
        -------
        string
            the item at given index.
        """
        return list(self.keys())[index]

    def getValue(self, index: int) -> int:
        """
        The getValue method takes an index as an input and returns the value at given index.

        PARAMETERS
        ----------
        index : int
            index is used for searching the value.

        RETURNS
        -------
        int
            the value at given index.
        """
        return list(self.values())[index]

    def getCount(self, item: str) -> int:
        """
        The getCount method takes an item as an input returns the value to which the specified item is mapped, or ""
        if this map contains no mapping for the key.

        PARAMETERS
        ----------
        item : string

        RETURNS
        -------
        int
            the value to which the specified item is mapped
        """
        return self[item]

    def getMaxItem(self) -> str:
        """
        The getMaxItem method loops through the entries and gets the entry with maximum value.

        RETURNS
        -------
        string
            the entry with maximum value.
        """
        maxValue = -1
        maxItem = ""
        for item in self:
            if self[item] > maxValue:
                maxValue = self[item]
                maxItem = item
        return maxItem

    def getMaxItemIncludeTheseOnly(self, includeTheseOnly: list) -> str:
        """
        Another getMaxItem method which takes a list of Strings. It loops through the items in this list
        and gets the item with maximum value.

        PARAMETERS
        ----------
        includeTheseOnly : list
            list of Strings.

        RETURNS
        -------
        string
            the item with maximum value.
        """
        maxValue = -1
        maxItem = ""
        for item in includeTheseOnly:
            frequency = 0
            if item in self:
                frequency = self[item]
            if frequency > maxValue:
                maxValue = frequency
                maxItem = item
        return maxItem

    def getProbability(self, item: str) -> float:
        """
        The getProbability method takes an item as an input returns the value to which the specified item is mapped over
        sum, or 0.0 if this map contains no mapping for the key.

        PARAMETERS
        ----------
        item : string
            is used to search for probability.

        RETURNS
        -------
        double
            the probability to which the specified item is mapped.
        """
        if item in self:
            return self[item] / self.__sum
        else:
            return 0.0

    def getProbabilityLaplaceSmoothing(self, item: str) -> float:
        """
        The getProbabilityLaplaceSmoothing method takes an item as an input returns the smoothed value to which the
        specified item is mapped over sum, or 1.0 over sum if this map contains no mapping for the key.
        PARAMETERS
        ----------
        item : string
            is used to search for probability.

        RETURNS
        -------
        double
            the smoothed probability to which the specified item is mapped.
        """
        if item in self:
            return (self[item] + 1) / (self.__sum + len(self) + 1)
        else:
            return 1.0 / (self.__sum + len(self) + 1)

    def entropy(self) -> float:
        """
        The entropy method loops through the values and calculates the entropy of these values.

        RETURNS
        -------
        double
            entropy value.
        """
        total = 0.0
        for count in self.values():
            probability = count / self.__sum
            total += -probability * math.log2(probability)
        return total
