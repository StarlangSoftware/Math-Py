from __future__ import annotations
import random
import Vector
import MatrixDimensionMismatch
import MatrixColumnMismatch


class Matrix(object):

    """
    Constructor of Matrix class which takes row and column numbers as inputs.

    PARAMETERS
    ----------
    row : int
        is used to create matrix.
    col : int
        is used to create matrix.
    """
    def __init__(self, row : int, col : int):
        self.row = row
        self.col = col
        self.initZeros()

    def initZeros(self):
        self.values = [[0 for j in range(self.col)] for i in range(self.row)]

    """
    Another initializer of Matrix class which takes minimum and maximum values as inputs.
    It creates new values list with given row and column numbers. Then fills in the
    positions with random numbers using minimum and maximum inputs.

    PARAMETERS
    ----------
    min : double 
        minimum value.
    max : double
        maximum value.
    """
    def initRandom(self, minValue : float, maxValue : float):
        self.values = [[random.uniform(minValue, maxValue) for j in range(self.col)] for i in range(self.row)]

    """
    Another constructor of Matrix class which takes size as input and creates new values list
    with using size input and assigns 1 to each element at the diagonal.
    """
    def initIdentity(self):
        self.initZeros()
        for i in range(self.row):
            self.values[i][i] = 1

    """
    The getter for the index at given rowNo and colNo of values list.

    PARAMETERS
    ----------
    rowNo : int 
        integer input for row number.
    colNo : int 
        integer input for column number.
        
    RETURNS
    -------
    double
        item at given index of values list.
    """
    def getValue(self, rowNo : int, colNo : int) -> float:
        return self.values[rowNo][colNo]

    """
    The setter for the value at given index of values list.

    PARAMETERS
    ----------
    rowNo : int 
        integer input for row number.
    colNo : int 
        integer input for column number.
    value : double
        is used to set at given index.
    """
    def setValue(self, rowNo : int, colNo : int, value : float):
        self.values[rowNo][colNo] = value

    """
    The addValue method adds the given value to the item at given index of values list.

    PARAMETERS
    ----------
    rowNo : int 
        integer input for row number.
    colNo : int 
        integer input for column number.
    value : double
        is used to add to given item at given index.
    """
    def addValue(self, rowNo : int, colNo : int, value : float):
        self.values[rowNo][colNo] += value

    """
     * The increment method adds 1 to the item at given index of values list.
     *
     * @param rowNo integer input for row number.
     * @param colNo integer input for column number.
    """
    def increment(self, rowNo : int, colNo : int):
        self.values[rowNo][colNo] += 1

    """
    The getter for the row variable.

    RETURNS
    -------
    int
        row number.
    """
    def getRow(self) -> int:
        return self.row

    """
    The getRowVector method returns the vector of values list at given row input.

    PARAMETERS
    ----------
    row : int 
        row integer input for row number.

    RETURNS
    -------
    Vector
        Vector of values list at given row input.
    """
    def getRowVector(self, row : int) -> Vector:
        rowVector = Vector.Vector()
        rowList = self.values[row]
        rowVector.initWithVector(rowList)
        return rowVector

    """
    The getter for the col variable.

    RETURNS
    -------
    int
        column number.
    """
    def getColumn(self) -> int:
        return self.col

    """
     * The getColumnVector method creates a Vector and adds items at given column number of values list
     * to the Vector.

    PARAMETERS
    ----------
    column : int
        column integer input for column number.
        
    RETURNS
    -------
    Vector
        Vector of given column number.
    """
    def getColumnVector(self, column : int) -> Vector:
        columnVector = Vector.Vector()
        for i in range(self.row):
            columnVector.add(self.values[i][column])
        return columnVector

    """
    The columnWiseNormalize method, first accumulates items column by column then divides items 
    by the summation.
    """
    def columnWiseNormalize(self):
        for i in range(self.row):
            total = sum(self.values[i])
            self.values[i][:] = [x / total for x in self.values[i]]

    """
    The multiplyWithConstant method takes a constant as an input and multiplies each item of values list
    with given constant.

    PARAMETERS
    ----------
    constant : double
        constant value to multiply items of values list.
    """
    def multiplyWithConstant(self, constant : float):
        for i in range(self.row):
            self.values[i][:] = [x * constant for x in self.values[i]]

    """
    The divideByConstant method takes a constant as an input and divides each item of values {@link java.lang.reflect.Array}
    with given constant.

    PARAMETERS
    ----------
    constant : double
        constant value to divide items of values list.
    """
    def divideByConstant(self, constant : float):
        for i in range(self.row):
            self.values[i][:] = [x / constant for x in self.values[i]]

    """
    The add method takes a Matrix as an input and accumulates values list with the
    corresponding items of given Matrix. If the sizes of both Matrix and values list do not match,
    it throws MatrixDimensionMismatch exception.

    PARAMETERS
    ----------
    m : Matrix
        Matrix type input.
    """
    def add(self, m: Matrix):
        if self.row != m.row or self.col != m.col:
            raise MatrixDimensionMismatch
        for i in range(self.row):
            for j in range(self.col):
                self.values[i][j] += m.values[i][j]

    """
    The add method which takes a row number and a Vector as inputs. It sums up the corresponding values at the given 
    row of values list and given Vector. If the sizes of both Matrix and values list do not match, it throws 
    MatrixColumnMismatch exception.

    PARAMETERS
    ----------
    rowNo : int
        integer input for row number.
    v : Vector    
        Vector type input.
    """
    def addRowVector(self, rowNo: int, v: Vector):
        if self.col != v.size():
            raise MatrixColumnMismatch
        for i in range(self.col):
            self.values[rowNo][i] += v.getValue(i)