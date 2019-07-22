from __future__ import annotations
import collections
import math


class DiscreteDistribution(collections.OrderedDict):

    """
    A constructor of DiscreteDistribution class which calls its super class.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sum = 0.0

    """
    The addItem method takes a String item as an input and if this map contains a mapping for the item it puts the item
    with given value + 1, else it puts item with value of 1.
    
    PARAMETERS
    ----------
    item : string 
        String input.
    """
    def addItem(self, item: str):
        if item in self:
            self[item] = self[item] + 1
        else:
            self[item] = 1
        self.sum = self.sum + 1

    """
    The removeItem method takes a String item as an input and if this map contains a mapping for the item it puts the 
    item with given value - 1, and if its value is 0, it removes the item.

    PARAMETERS
    ----------
    item : string 
        String input.
    """
    def removeItem(self, item: str):
        if item in self:
            self[item] = self[item] - 1
            if self[item] == 0:
                self.pop(item)

    """
    The addDistribution method takes a DiscreteDistribution as an input and loops through the entries in this 
    distribution and if this map contains a mapping for the entry it puts the entry with its value + entry, 
    else it puts entry with its value. It also accumulates the values of entries and assigns to the sum variable.

    PARAMETERS
    ----------
    distribution : DiscreteDistribution 
        DiscreteDistribution type input.
    """
    def addDistribution(self, distribution: DiscreteDistribution):
        for entry in distribution:
            if entry in self:
                self[entry] = self[entry] + distribution[entry]
            else:
                self[entry] = distribution[entry]
            self.sum += distribution[entry]

    """
    The removeDistribution method takes a DiscreteDistribution as an input and loops through the entries in this 
    distribution and if this map contains a mapping for the entry it puts the entry with its key - value, else it 
    removes the entry. It also decrements the value of entry from sum and assigns to the sum variable.

    PARAMETERS
    ----------
    distribution : DiscreteDistribution 
        DiscreteDistribution type input.
    """
    def removeDistribution(self, distribution: DiscreteDistribution):
        for entry in distribution:
            if self[entry] - distribution[entry] != 0:
                self[entry] -= distribution[entry]
            else:
                self.pop(entry)
            self.sum -= distribution[entry]

    """
    The getter for sum variable.
    
    RETURNS
    -------
    double
        sum
    """
    def getSum(self) -> float:
        return self.sum

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
    def getIndex(self, item: str) -> int:
        return list(self.keys()).index(item)

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
    def containsItem(self, item: str) -> bool:
        return item in self

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
    def getItem(self, index: int) -> str:
        return list(self.keys())[index]

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
    def getValue(self, index: int) -> str:
        return list(self.values())[index]

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
    def getCount(self, item: str) -> int:
        return self[item]

    """
    The getMaxItem method loops through the entries and gets the entry with maximum value.

    RETURNS
    -------
    string
        the entry with maximum value.
    """
    def getMaxItem(self) -> str:
        maxValue = -1
        maxItem = ""
        for item in self:
            if self[item] > maxValue:
                maxValue = self[item]
                maxItem = item
        return maxItem

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
    def getMaxItemIncludeTheseOnly(self, includeTheseOnly: list) -> str:
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
    def getProbability(self, item: str) -> float:
        if item in self:
            return self[item] / sum
        else:
            return 0.0

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
    def getProbabilityLaplaceSmoothing(self, item: str) -> float:
        if item in self:
            return (self[item] + 1) / (self.sum + len(self) + 1)
        else:
            return 1.0 / (self.sum + len(self) + 1)

    """
    The entropy method loops through the values and calculates the entropy of these values.

    RETURNS
    -------
    double
        entropy value.
    """
    def entropy(self) -> float:
        total = 0.0
        for count in self.values():
            probability = count / sum
            total += -probability * math.log2(probability)
        return total
