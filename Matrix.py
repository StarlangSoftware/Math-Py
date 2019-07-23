from __future__ import annotations
import random
import Vector
import MatrixDimensionMismatch
import MatrixColumnMismatch
import MatrixRowMismatch
import MatrixRowColumnMismatch
import MatrixNotSquare


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

    """
    The subtract method takes a Matrix as an input and subtracts from values list the
    corresponding items of given Matrix. If the sizes of both Matrix and values list do not match,
    it throws {@link MatrixDimensionMismatch} exception.

    PARAMETERS
    ----------
    m : Matrix
        Matrix type input.
    """
    def subtract(self, m: Matrix):
        if self.row != m.row or self.col != m.col:
            raise MatrixDimensionMismatch
        for i in range(self.row):
            for j in range(self.col):
                self.values[i][j] -= m.values[i][j]

    """
    The multiplyWithVectorFromLeft method takes a Vector as an input and creates a result list.
    Then, multiplies values of input Vector starting from the left side with the values list,
    accumulates the multiplication, and assigns to the result list. If the sizes of both Vector
    and row number do not match, it throws MatrixRowMismatch exception.

    PARAMETERS
    ----------
    v : Vector
        Vector type input.
        
    RETURNS
    -------
    Vector
        Vector that holds the result.
    """
    def multiplyWithVectorFromLeft(self, v: Vector) -> Vector:
        if self.row != v.size():
            raise MatrixRowMismatch
        result = Vector.Vector()
        for i in range(self.col):
            total = 0.0
            for j in range(self.row):
                total += v.getValue(j) * self.values[j][i]
            result.add(total)
        return result

    """
    The multiplyWithVectorFromRight method takes a Vector as an input and creates a result list.
    Then, multiplies values of input Vector starting from the right side with the values list,
    accumulates the multiplication, and assigns to the result list. If the sizes of both Vector
    and row number do not match, it throws MatrixColumnMismatch exception.

    PARAMETERS
    ----------
    v : Vector
        Vector type input.
        
    RETURNS
    -------
    Vector
        Vector that holds the result.
    """
    def multiplyWithVectorFromRight(self, v: Vector) -> Vector:
        if self.col != v.size():
            raise MatrixColumnMismatch
        result = Vector.Vector()
        for i in range(self.row):
            total = 0.0
            for j in range(self.col):
                total += v.getValue(j) * self.values[i][j]
            result.add(total)
        return result

    """
    The columnSum method takes a column number as an input and accumulates items at given column number of values
    list.

    PARAMETERS
    ----------
    columnNo : int
        Column number input.
        
    RETURNS
    -------
    double
        summation of given column of values list.
    """
    def columnSum(self, columnNo: int) -> float:
        total = 0
        for i in range(self.row):
            total += self.values[i][columnNo]
        return total

    """
    The sumOfRows method creates a mew result Vector and adds the result of columnDum method's corresponding
    index to the newly created result Vector.

    RETURNS
    -------
    Vector
        Vector that holds column sum.
    """
    def sumOfRows(self) -> Vector:
        result = Vector.Vector()
        for i in range(self.col):
            result.add(self.columnSum(i))
        return result

    """
    The rowSum method takes a row number as an input and accumulates items at given row number of values list.

     * @param rowNo Row number input.
     * @return summation of given row of values {@link java.lang.reflect.Array}.
    """
    def rowSum(self, rowNo: int) -> float:
        return sum(self.values[rowNo])

    """
    The multiply method takes a Matrix as an input. First it creates a result Matrix and puts the
    accumulatated multiplication of values list and given Matrix into result
    Matrix. If the size of Matrix's row size and values list's column size do not match,
    it throws MatrixRowColumnMismatch exception.

    PARAMETERS
    ----------
    m : Matrix
        Matrix type input.

    RETURNS
    -------
    Matrix
        result Matrix.
    """
    def multiply(self, m: Matrix) -> Matrix:
        if self.col != m.row:
            raise MatrixRowColumnMismatch
        result = Matrix(self.row, m.col)
        for i in range(self.row):
            for j in range(m.col):
                sum = 0.0
                for k in range(self.col):
                    sum += self.values[i][k] * m.values[k][j]
                result.values[i][j] = sum
        return result

    """
    The elementProduct method takes a Matrix as an input and performs element wise multiplication. Puts result
    to the newly created Matrix. If the size of Matrix's row and column size does not match with the values
    list's row and column size, it throws MatrixDimensionMismatch exception.

    PARAMETERS
    ----------
    m : Matrix
        Matrix type input.

    RETURNS
    -------
    Matrix
        result Matrix.
    """
    def elementProduct(self, m: Matrix) -> Matrix:
        if self.row != m.row or self.col != m.col:
            raise MatrixDimensionMismatch
        result = Matrix(self.row, self.col)
        for i in range(self.row):
            for j in range(self.col):
                result.values[i][j] = self.values[i][j] * m.values[i][j]
        return result

    """
    The sumOfElements method accumulates all the items in values list and
    returns this summation.

    RETURNS
    -------
    float
        sum of the items of values list.
    """
    def sumOfElements(self) -> float:
        total = 0.0
        for i in range(self.row):
            total += sum(self.values[i])
        return total

    """
    The trace method accumulates items of values list at the diagonal.

    RETURNS
    -------
    float
        sum of items at diagonal.
    """
    def trace(self) -> float:
        if self.row != self.col:
            raise MatrixNotSquare
        total = 0.0
        for i in range(self.row):
            total += self.values[i][i]
        return total

    """
    The transpose method creates a new Matrix, then takes the transpose of values list
    and puts transposition to the Matrix.

    RETURNS
    -------
    Matrix
        Matrix type output.
    """
    def transpose(self) -> Matrix:
        result = Matrix(self.col, self.row)
        for i in range(self.row):
            for j in range(self.col):
                result.values[j][i] = self.values[i][j]
        return result

    """
    The partial method takes 4 integer inputs; rowStart, rowEnd, colStart, colEnd and creates a Matrix size of
    rowEnd - rowStart + 1 x colEnd - colStart + 1. Then, puts corresponding items of values list
    to the new result Matrix.

    PARAMETERS
    ----------
    rowStart : int
        integer input for defining starting index of row.
    rowEnd : int  
        integer input for defining ending index of row.
    colStart : int
        integer input for defining starting index of column.
    colEnd : int  
        integer input for defining ending index of column.

    RETURNS
    -------
    Matrix
        result Matrix.
    """
    def partial(self, rowStart: int, rowEnd: int, colStart: int, colEnd: int) -> Matrix:
        result = Matrix(rowEnd - rowStart + 1, colEnd - colStart + 1)
        for i in range(rowStart, rowEnd + 1):
            for j in range(colStart, colEnd + 1):
                result.values[i - rowStart][j - colStart] = self.values[i][j]
        return result
