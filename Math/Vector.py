from __future__ import annotations
import math
from Math import VectorSizeMismatch


class Vector(object):

    def __init__(self):
        self.values = []
        self.size = 0

    """
    A constructor of Vector class which takes a list values as an input. Then, initializes
    values list and size variable with given input and its size.

    Parameters
    ----------
    values : list
        list input.
    """
    def initWithVector(self, values: list):
        self.values = values
        self.size = len(values)

    """
    Another constructor of Vector class which takes integer size and double x as inputs. Then, initializes size
    variable with given size input and creates new values list and adds given input x to values list.

    Parameters
    ----------
    size : int
        list size.
    x : double   
        item to add values list.
    """
    def initAllSame(self, size: int, x: float):
        self.size = size
        self.values = []
        for i in range(size):
            self.values.append(x)

    """
    Another constructor of Vector class which takes integer size, integer index and double x as inputs. 
    Then, initializes size variable with given size input and creates new values list and adds 0.0 to 
    values list. Then, sets the item of values list at given index as given input x.

    Parameters
    ----------
    size : int 
        list size.
    index : int 
        to set a particular item.
    x : double    
        item to add values list's given index.
    """
    def initAllZerosExceptOne(self, size: int, index: int, x: float):
        self.size = size
        self.values = []
        for i in range(size):
            self.values.append(0.0)
        self.values[index] = x

    """
    The biased method creates a list result, add adds each item of values list into the result list.
    Then, insert 1.0 to 0th position and return result list.
    
    Returns
    ----------
    list
        result list.
    """
    def biased(self):
        result = Vector()
        for value in self.values:
            result.add(value)
        result.insert(0, 1.0)
        return result

    """
    The add method adds given input to the values {@link ArrayList} and increments the size variable by one.

    Parameters
    ----------
    x : double 
        input to add values list.
    """
    def add(self, x: float):
        self.values.append(x)
        self.size = self.size + 1

    """
    The insert method puts given input to the given index of values list and increments the size variable by one.

    Parameters
    ----------
    pos : int 
        index to insert input.
    x : double  
        input to insert to given index of values list.
    """
    def insert(self, pos: int, x: float):
        self.values.insert(pos, x)
        self.size = self.size + 1

    """
    The remove method deletes the item at given input position of values list and decrements the size variable by one.

    Parameters
    ----------
    pos : int 
        index to remove from values list.
    """
    def remove(self, pos: int):
        self.values.pop(pos)
        self.size = self.size - 1

    """
    The clear method sets all the elements of values list to 0.
    """
    def clear(self):
        for i in range(len(self.values)):
            self.values[i] = 0

    """
    The maxIndex method gets the first item of values list as maximum item, then it loops through the indices
    and if a greater value than the current maximum item comes, it updates the maximum item and returns the final
    maximum item's index.

    Returns
    ----------
    int
        final maximum item's index.
    """
    def maxIndex(self) -> int:
        index = 0
        maxValue = self.values[0]
        for i in range(1, self.size):
            if self.values[i] > maxValue:
                maxValue = self.values[i]
                index = i
        return index

    """
    The sigmoid method loops through the values list and sets each ith item with sigmoid function, i.e
    1 / (1 + Math.exp(-values.get(i))), i ranges from 0 to size.
    """
    def sigmoid(self):
        for i in range (self.size):
            self.values[i] = 1 / (1 + math.exp(-self.values[i]))

    """
    The skipVector method takes a mod and a value as inputs. It creates a new result Vector, and assigns given input value to i.
    While i is less than the size, it adds the ith item of values {@link ArrayList} to the result and increments i by given mod input.

    Parameters
    ----------
    mod : int   
        integer input.
    value : int
        integer input.

    Returns
    ----------
    Vector
        result Vector.
    """
    def skipVector(self, mod: int, value: int) -> Vector:
        result = Vector()
        i = value
        while i < self.size:
            result.add(self.values[i])
            i += mod
        return result

    """
    The add method takes a Vector v as an input. It sums up the corresponding elements of both given vector's
    values list and values list and puts result back to the values list.

    Parameters
    ----------
    v : Vector
        Vector to add.
    """
    def addVector(self, v: Vector):
        if self.size != v.size:
            raise VectorSizeMismatch
        for i in range(self.size):
            self.values[i] = self.values[i] + v.values[i]

    """
    The subtract method takes a Vector v as an input. It subtracts the corresponding elements of given vector's
    values list from values list and puts result back to the values list.

    Parameters
    ----------
    v : Vector
        Vector to subtract from values list.
    """
    def subtract(self, v: Vector):
        if self.size != v.size:
            raise VectorSizeMismatch
        for i in range(self.size):
            self.values[i] = self.values[i] - v.values[i]

    """
    The difference method takes a Vector v as an input. It creates a new Vector result, then
    subtracts the corresponding elements of given vector's values list from values list and puts
    result back to the result.

    Parameters
    ----------
    v : Vector
        Vector to find difference from values list.
    
    Returns
    ----------
    Vector
        new Vector with result list.
    """
    def difference(self, v: Vector) -> Vector:
        if self.size != v.size:
            raise VectorSizeMismatch
        result = Vector()
        for i in range(self.size):
            result.add(self.values[i] - v.values[i])
        return result

    """
    The dotProduct method takes a Vector v as an input. It creates a new double variable result, then
    multiplies the corresponding elements of given vector's values list with values list and assigns
    the multiplication to the result.

    Parameters
    ----------
    v : Vector
        Vector to find dot product.

    Returns
    ----------
    double 
        result.
    """
    def dotProduct(self, v: Vector) -> float:
        if self.size != v.size:
            raise VectorSizeMismatch
        result = 0
        for i in range (self.size):
            result += self.values[i] * v.values[i]
        return result

    """
    The dotProduct method creates a new double variable result, then squares the elements of values list and assigns
    the accumulation to the result.

    Returns
    ----------
    double 
        result.
    """
    def dotProductWithSelf(self) -> float:
        result = 0
        for i in range (self.size):
            result += self.values[i] * self.values[i]
        return result

    """
    The elementProduct method takes a Vector v as an input. It creates a new Vector result, then
    multiplies the corresponding elements of given vector's values list with values list and adds
    the multiplication to the result list. 

    Parameters
    ----------
    v : Vector
        Vector to find dot product.

    Returns
    ----------
    Vector 
        with result list.
    """
    def elementProduct(self, v: Vector) -> Vector:
        if self.size != v.size:
            raise VectorSizeMismatch
        result = Vector()
        for i in range(self.size):
            result.add(self.values[i] * v.values[i])
        return result

    """
    The divide method takes a double value as an input and divides each item of values list with given value.

    Parameters
    ----------
    value : double
        is used to divide items of values list.
    """
    def divide(self, value: float):
        for i in range(self.size):
            self.values[i] = self.values[i] / value

    """
    The multiply method takes a double value as an input and multiplies each item of values list with given value.

    Parameters
    ----------
    value : double
        is used to multiply items of values list.
    """
    def multiply(self, value: float):
        for i in range(self.size):
            self.values[i] = self.values[i] * value

    """
    The product method takes a double value as an input and creates a new result {@link Vector}, then multiplies each
    item of values {@link ArrayList} with given value and adds to the result {@link Vector}.

    Parameters
    ----------
    value : double
        is used to multiply items of values list.
        
    Returns
    ----------
    Vector 
        Vector result.
    """
    def product(self, value: float) -> Vector:
        result = Vector()
        for i in range(self.size):
            result.add(self.values[i] * value)
        return result

    """
    The l1Normalize method is used to apply Least Absolute Errors, it accumulates items of values list and sets
    each item by dividing it by the summation value.
    """
    def l1Normalize(self):
        sum = 0
        for i in range(self.size):
            sum += self.values[i]
        for i in range(self.size):
            self.values[i] = self.values[i] / sum

    """
    The l2Norm method is used to apply Least Squares, it accumulates second power of each items of values {@link ArrayList}
    and returns the square root of this summation.

    Returns
    ----------
    double
        square root of this summation.
    """
    def l2Norm(self) -> float:
        sum = 0
        for i in range(self.size):
            sum += self.values[i] ** 2
        return math.sqrt(sum)

    """
    The cosineSimilarity method takes a Vector v as an input and returns the result of dotProduct(v) / l2Norm() / v.l2Norm().

    Parameters
    ----------
    v : Vector 
        input.
        
    Returns
    ----------
    double
        dotProduct(v) / l2Norm() / v.l2Norm()
    """
    def cosineSimilarity(self, v: Vector) -> float:
        if self.size != v.size:
            raise VectorSizeMismatch
        return self.dotProduct(v) / self.l2Norm() / v.l2Norm()

    """
    The size method returns the size of the values list

    Returns
    ----------
    int
        size of the values list
    """
    def size(self) -> int:
        return len(self.values)

    """
    Getter for the item at given index of values list

    Parameters
    ----------
    index : int
        index used to get an item.

    Returns
    ----------
    item
        the item at given index.
    """
    def getValue(self, index: int) -> float:
        return self.values[index]

    """
    Setter for the setting the value at given index of values list.

    Parameters
    ----------
    index : int
        index to set.
    value : item 
        is used to set the given index
    """
    def setValue(self, index: int, value: float):
        self.values[index] = value

    """
    The addValue method adds the given value to the item at given index of values {@link ArrayList}.

    Parameters
    ----------
    index : int
        index to add the given value.
    value : item
        value to add to given index.
    """
    def addValue(self, index: int, value: float):
        self.values[index] += value