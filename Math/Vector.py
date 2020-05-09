from __future__ import annotations
import math

from Math.VectorSizeMismatch import VectorSizeMismatch


class Vector(object):

    __size: int
    __values: list

    def __init__(self, valuesOrSize=None, initial=None):
        """
        A constructor of Vector class which takes a list values as an input. Then, initializes
        values list and size variable with given input and its size.

        PARAMETERS
        ----------
        valuesOrSize
            list input or size.
        initial
            initial value for each element
        """
        if valuesOrSize is None:
            self.__values = []
            self.__size = 0
        elif isinstance(valuesOrSize, list):
            self.__values = valuesOrSize.copy()
            self.__size = len(valuesOrSize)
        else:
            self.initAllSame(valuesOrSize, initial)

    def initAllSame(self, size: int, x: float):
        """
        Another constructor of Vector class which takes integer size and double x as inputs. Then, initializes size
        variable with given size input and creates new values list and adds given input x to values list.

        PARAMETERS
        ----------
        size : int
            list size.
        x : double
            item to add values list.
        """
        self.__size = size
        self.__values = []
        for i in range(size):
            self.__values.append(x)

    def initAllZerosExceptOne(self, size: int, index: int, x: float):
        """
        Another constructor of Vector class which takes integer size, integer index and double x as inputs.
        Then, initializes size variable with given size input and creates new values list and adds 0.0 to
        values list. Then, sets the item of values list at given index as given input x.

        PARAMETERS
        ----------
        size : int
            list size.
        index : int
            to set a particular item.
        x : double
            item to add values list's given index.
        """
        self.__size = size
        self.__values = []
        for i in range(size):
            self.__values.append(0.0)
        self.__values[index] = x

    def biased(self) -> Vector:
        """
        The biased method creates a list result, add adds each item of values list into the result list.
        Then, insert 1.0 to 0th position and return result list.

        RETURNS
        -------
        list
            result list.
        """
        result = Vector()
        for value in self.__values:
            result.add(value)
        result.insert(0, 1.0)
        return result

    def add(self, x: float):
        """
        The add method adds given input to the values {@link ArrayList} and increments the size variable by one.

        PARAMETERS
        ----------
        x : double
            input to add values list.
        """
        self.__values.append(x)
        self.__size = self.__size + 1

    def insert(self, pos: int, x: float):
        """
        The insert method puts given input to the given index of values list and increments the size variable by one.

        PARAMETERS
        ----------
        pos : int
            index to insert input.
        x : double
            input to insert to given index of values list.
        """
        self.__values.insert(pos, x)
        self.__size = self.__size + 1

    def remove(self, pos: int):
        """
        The remove method deletes the item at given input position of values list and decrements the size variable by
        one.

        PARAMETERS
        ----------
        pos : int
            index to remove from values list.
        """
        self.__values.pop(pos)
        self.__size = self.__size - 1

    def clear(self):
        """
        The clear method sets all the elements of values list to 0.
        """
        for i in range(len(self.__values)):
            self.__values[i] = 0

    def sumOfElements(self) -> float:
        """
        The sumOfElements method sums up all elements in the vector.

        RETURNS
        -------
        float
            Sum of all elements in the vector.
        """
        total = 0
        for i in range(self.__size):
            total += self.__values[i]
        return total

    def maxIndex(self) -> int:
        """
        The maxIndex method gets the first item of values list as maximum item, then it loops through the indices
        and if a greater value than the current maximum item comes, it updates the maximum item and returns the final
        maximum item's index.

        RETURNS
        -------
        int
            final maximum item's index.
        """
        index = 0
        maxValue = self.__values[0]
        for i in range(1, self.__size):
            if self.__values[i] > maxValue:
                maxValue = self.__values[i]
                index = i
        return index

    def sigmoid(self):
        """
        The sigmoid method loops through the values list and sets each ith item with sigmoid function, i.e
        1 / (1 + Math.exp(-values.get(i))), i ranges from 0 to size.
        """
        for i in range(self.__size):
            self.__values[i] = 1 / (1 + math.exp(-self.__values[i]))

    def skipVector(self, mod: int, value: int) -> Vector:
        """
        The skipVector method takes a mod and a value as inputs. It creates a new result Vector, and assigns given input
        value to i. While i is less than the size, it adds the ith item of values {@link ArrayList} to the result and
        increments i by given mod input.

        PARAMETERS
        ----------
        mod : int
            integer input.
        value : int
            integer input.

        RETURNS
        -------
        Vector
            result Vector.
        """
        result = Vector()
        i = value
        while i < self.__size:
            result.add(self.__values[i])
            i += mod
        return result

    def addVector(self, v: Vector):
        """
        The add method takes a Vector v as an input. It sums up the corresponding elements of both given vector's
        values list and values list and puts result back to the values list.

        PARAMETERS
        ----------
        v : Vector
            Vector to add.
        """
        if self.__size != v.__size:
            raise VectorSizeMismatch
        for i in range(self.__size):
            self.__values[i] = self.__values[i] + v.__values[i]

    def subtract(self, v: Vector):
        """
        The subtract method takes a Vector v as an input. It subtracts the corresponding elements of given vector's
        values list from values list and puts result back to the values list.

        PARAMETERS
        ----------
        v : Vector
            Vector to subtract from values list.
        """
        if self.__size != v.__size:
            raise VectorSizeMismatch
        for i in range(self.__size):
            self.__values[i] = self.__values[i] - v.__values[i]

    def difference(self, v: Vector) -> Vector:
        """
        The difference method takes a Vector v as an input. It creates a new Vector result, then
        subtracts the corresponding elements of given vector's values list from values list and puts
        result back to the result.

        PARAMETERS
        ----------
        v : Vector
            Vector to find difference from values list.

        RETURNS
        -------
        Vector
            new Vector with result list.
        """
        if self.__size != v.__size:
            raise VectorSizeMismatch
        result = Vector()
        for i in range(self.__size):
            result.add(self.__values[i] - v.__values[i])
        return result

    def dotProduct(self, v: Vector) -> float:
        """
        The dotProduct method takes a Vector v as an input. It creates a new double variable result, then
        multiplies the corresponding elements of given vector's values list with values list and assigns
        the multiplication to the result.

        PARAMETERS
        ----------
        v : Vector
            Vector to find dot product.

        RETURNS
        -------
        double
            result.
        """
        if self.__size != v.__size:
            raise VectorSizeMismatch
        result = 0
        for i in range(self.__size):
            result += self.__values[i] * v.__values[i]
        return result

    def dotProductWithSelf(self) -> float:
        """
        The dotProduct method creates a new double variable result, then squares the elements of values list and assigns
        the accumulation to the result.

        RETURNS
        -------
        double
            result.
        """
        result = 0
        for i in range(self.__size):
            result += self.__values[i] * self.__values[i]
        return result

    def elementProduct(self, v: Vector) -> Vector:
        """
        The elementProduct method takes a Vector v as an input. It creates a new Vector result, then
        multiplies the corresponding elements of given vector's values list with values list and adds
        the multiplication to the result list.

        PARAMETERS
        ----------
        v : Vector
            Vector to find dot product.

        RETURNS
        -------
        Vector
            with result list.
        """
        if self.__size != v.__size:
            raise VectorSizeMismatch
        result = Vector()
        for i in range(self.__size):
            result.add(self.__values[i] * v.__values[i])
        return result

    def divide(self, value: float):
        """
        The divide method takes a double value as an input and divides each item of values list with given value.

        PARAMETERS
        ----------
        value : double
            is used to divide items of values list.
        """
        for i in range(self.__size):
            self.__values[i] = self.__values[i] / value

    def multiply(self, value: float):
        """
        The multiply method takes a double value as an input and multiplies each item of values list with given value.

        PARAMETERS
        ----------
        value : double
            is used to multiply items of values list.
        """
        for i in range(self.__size):
            self.__values[i] = self.__values[i] * value

    def product(self, value: float) -> Vector:
        """
        The product method takes a double value as an input and creates a new result {@link Vector}, then multiplies
        each item of values list with given value and adds to the result {@link Vector}.

        PARAMETERS
        ----------
        value : double
            is used to multiply items of values list.

        RETURNS
        -------
        Vector
            Vector result.
        """
        result = Vector()
        for i in range(self.__size):
            result.add(self.__values[i] * value)
        return result

    def l1Normalize(self):
        """
        The l1Normalize method is used to apply Least Absolute Errors, it accumulates items of values list and sets
        each item by dividing it by the summation value.
        """
        total = 0
        for i in range(self.__size):
            total += self.__values[i]
        for i in range(self.__size):
            self.__values[i] = self.__values[i] / total

    def l2Norm(self) -> float:
        """
        The l2Norm method is used to apply Least Squares, it accumulates second power of each items of values list
        and returns the square root of this summation.

        RETURNS
        -------
        float
            square root of this summation.
        """
        total = 0
        for i in range(self.__size):
            total += self.__values[i] ** 2
        return math.sqrt(total)

    def cosineSimilarity(self, v: Vector) -> float:
        """
        The cosineSimilarity method takes a Vector v as an input and returns the result of dotProduct(v)
        / l2Norm() / v.l2Norm().

        PARAMETERS
        ----------
        v : Vector
            input.

        RETURNS
        -------
        float
            dotProduct(v) / l2Norm() / v.l2Norm()
        """
        if self.__size != v.__size:
            raise VectorSizeMismatch
        return self.dotProduct(v) / self.l2Norm() / v.l2Norm()

    def size(self) -> int:
        """
        The size method returns the size of the values list

        RETURNS
        -------
        int
            size of the values list
        """
        return len(self.__values)

    def getValue(self, index: int) -> float:
        """
        Getter for the item at given index of values list

        PARAMETERS
        ----------
        index : int
            index used to get an item.

        RETURNS
        -------
        item
            the item at given index.
        """
        return self.__values[index]

    def setValue(self, index: int, value: float):
        """
        Setter for the setting the value at given index of values list.

        PARAMETERS
        ----------
        index : int
            index to set.
        value : item
            is used to set the given index
        """
        self.__values[index] = value

    def addValue(self, index: int, value: float):
        """
        The addValue method adds the given value to the item at given index of values list.

        PARAMETERS
        ----------
        index : int
            index to add the given value.
        value : item
            value to add to given index.
        """
        self.__values[index] += value
