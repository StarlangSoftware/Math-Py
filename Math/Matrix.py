from __future__ import annotations
import random
import math
from Math.MatrixNotPositiveDefinite import MatrixNotPositiveDefinite
from Math.MatrixNotSquare import MatrixNotSquare
from Math.Eigenvector import Eigenvector
from Math.MatrixDimensionMismatch import MatrixDimensionMismatch
from Math.Vector import Vector
from Math.MatrixRowMismatch import MatrixRowMismatch
from Math.DeterminantZero import DeterminantZero
from Math.MatrixRowColumnMismatch import MatrixRowColumnMismatch
from Math.MatrixColumnMismatch import MatrixColumnMismatch
from Math.MatrixNotSymmetric import MatrixNotSymmetric


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
    The clone method creates new Matrix and copies the content of values list into new matrix.

    RETURNS
    -------
    Matrix
        Matrix which is the copy of values list.
    """
    def clone(self) -> Matrix:
        result = Matrix(self.row, self.col)
        for i in range(self.row):
            for j in range(self.col):
                result.values[i][j] = self.values[i][j]
        return result


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
        rowVector = Vector()
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
    def getColumnVector(self, column : int) -> list:
        columnVector = []
        for i in range(self.row):
            columnVector.append(self.values[i][column])
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
        result = Vector()
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
        result = Vector()
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
        result = Vector()
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

    """
    The isSymmetric method compares each item of values list at positions (i, j) with (j, i)
    and returns true if they are equal, false otherwise.

    RETURNS
    -------
    bool
        true if items are equal, false otherwise.
    """
    def isSymmetric(self) -> bool:
        if self.row != self.col:
            raise MatrixNotSquare
        for i in range(self.row - 1):
            for j in range(self.row):
                if self.values[i][j] != self.values[j][i]:
                    return False
        return True

    """
    The determinant method first creates a new list, and copies the items of  values
    list into new list. Then, calculates the determinant of this
    new list.

    RETURNS
    -------
    float
        determinant of values list.
    """
    def determinant(self) -> float:
        if self.row != self.col:
            raise MatrixNotSquare
        det = 1.0
        copy = self.clone()
        for i in range(self.row):
            det *= copy.values[i][i]
            if det == 0.0:
                break
            for j in range(i + 1, self.row):
                ratio = copy.values[j][i] / copy.values[i][i]
                for k in range(i, self.col):
                    copy.values[j][k] = copy.values[j][k] - copy.values[i][k] * ratio
        return det

    """
    The inverse method finds the inverse of values list.
    """
    def inverse(self):
        if self.row != self.col:
            raise MatrixNotSquare
        b = Matrix(self.row, self.row)
        indxc = []
        indxr = []
        ipiv = []
        for j in range(self.row):
            ipiv.append(0)
        for i in range(1, self.row + 1):
            big = 0.0
            irow = -1
            icol = -1
            for j in range(1, self.row + 1):
                if ipiv[j - 1] != 1:
                    for k in range(1, self.row + 1):
                        if ipiv[k - 1] == 0:
                            if abs(self.values[j - 1][k - 1]) >= big:
                                big = abs(self.values[j - 1][k - 1])
                                irow = j
                                icol = k
            if irow == -1 or icol == -1:
                raise DeterminantZero
            ipiv[icol - 1] = ipiv[icol - 1] + 1
            if irow != icol:
                for l in range(1, self.row + 1):
                    dum = self.values[irow - 1][l - 1]
                    self.values[irow - 1][l - 1] = self.values[icol - 1][l - 1]
                    self.values[icol - 1][l - 1] = dum
                for l in range(1, self.row + 1):
                    dum = b.values[irow - 1][l - 1]
                    b.values[irow - 1][l - 1] = b.values[icol - 1][l - 1]
                    b.values[icol - 1][l - 1] = dum
            indxr.append(irow)
            indxc.append(icol)
            if self.values[icol - 1][icol - 1] == 0:
                raise DeterminantZero
            pivinv = 1.0 / self.values[icol - 1][icol - 1]
            self.values[icol - 1][icol - 1] = 1.0
            for l in range (1, self.row + 1):
                self.values[icol - 1][l - 1] = self.values[icol - 1][l - 1] * pivinv
            for l in range(1, self.row + 1):
                b.values[icol - 1][l - 1] = b.values[icol - 1][l - 1] * pivinv
            for ll in range(1, self.row + 1):
                if ll != icol:
                    dum = self.values[ll - 1][icol - 1]
                    self.values[ll - 1][icol - 1] = 0.0
                    for l in range(1, self.row + 1):
                        self.values[ll - 1][l - 1] = self.values[ll - 1][l - 1] - self.values[icol - 1][l - 1] * dum
                    for l in range(1, self.row + 1):
                        b.values[ll - 1][l - 1] = b.values[ll - 1][l - 1] - b.values[icol - 1][l - 1] * dum
        for l in range(self.row, 0, -1):
            if indxr[l - 1] != indxc[l - 1]:
                for k in range(1, self.row + 1):
                    dum = self.values[k - 1][indxr[l - 1] - 1]
                    self.values[k - 1][indxr[l - 1] - 1] = self.values[k - 1][indxc[l - 1] - 1]
                    self.values[k - 1][indxc[l - 1] - 1] = dum

    """
    The choleskyDecomposition method creates a new Matrix and puts the Cholesky Decomposition of values Array
    into this Matrix. Also, it throws MatrixNotSymmetric exception if it is not symmetric and
    MatrixNotPositiveDefinite exception if the summation is negative.

    RETURNS
    -------
    Matrix
        Matrix type output.
    """
    def choleskyDecomposition(self) -> Matrix:
        if not self.isSymmetric():
            raise MatrixNotSymmetric
        b = Matrix(self.row, self.col)
        for i in range(self.row):
            for j in range(i, self.row):
                total = self.values[i][j]
                for k in range(i - 1, -1, -1):
                    total -= self.values[i][k] * self.values[j][k]
                if i == j:
                    if total <= 0.0:
                        raise MatrixNotPositiveDefinite
                    b.values[i][i] = math.sqrt(total)
                else:
                    b.values[j][i] = total / b.values[i][i]
        return b

    """
    The rotate method rotates values list according to given inputs.

    PARAMETERS
    ----------
    s : double
        double input.
    tau : double 
        double input.
    i : int  
        integer input.
    j : int  
        integer input.
    k : int  
        integer input.
    l : int  
        integer input.
    """
    def __rotate(self, s: float, tau: float, i: int, j: int, k: int, l: int):
        g = self.values[i][j]
        h = self.values[k][l]
        self.values[i][j] = g - s * (h + g * tau)
        self.values[k][l] = h + s * (g - h * tau)

    """
    The characteristics method finds and returns a sorted list of Eigenvecto}s. And it throws
    MatrixNotSymmetric exception if it is not symmetric.

    RETURNS
    -------
    list
        A sorted list of Eigenvectors.
    """
    def characteristics(self) -> list:
        if not self.isSymmetric():
            raise MatrixNotSymmetric
        matrix1 = self.clone()
        v = Matrix(self.row, self.row)
        v.initIdentity()
        d = []
        b = []
        z = []
        EPS = 0.000000000000000001
        for ip in range(self.row):
            b.append(matrix1.values[ip][ip])
            d.append(matrix1.values[ip][ip])
            z.append(0.0)
        for i in range(1, 51):
            sm = 0.0
            for ip in range(self.row - 1):
                for iq in range(ip + 1, self.row):
                    sm += abs(matrix1.values[ip][iq])
            if sm == 0.0:
                break
            if i < 4:
                threshold = 0.2 * sm / (self.row ** 2)
            else:
                threshold = 0.0
            for ip in range(self.row - 1):
                for iq in range(ip + 1, self.row):
                    g = 100.0 * abs(matrix1.values[ip][iq])
                    if i > 4 and g <= EPS * abs(d[ip]) and g <= EPS * abs(d[iq]):
                        matrix1.values[ip][iq] = 0.0
                    else:
                        if abs(matrix1.values[ip][iq]) > threshold:
                            h = d[iq] - d[ip]
                            if g <= EPS * abs(h):
                                t = matrix1.values[ip][iq] / h
                            else:
                                theta = 0.5 * h / matrix1.values[ip][iq]
                                t = 1.0 / (abs(theta) + math.sqrt(1.0 + theta ** 2))
                                if theta < 0.0:
                                    t = -t
                            c = 1.0 / math.sqrt(1 + t ** 2)
                            s = t * c
                            tau = s / (1.0 + c)
                            h = t * matrix1.values[ip][iq]
                            z[ip] -= h
                            z[iq] += h
                            d[ip] -= h
                            d[iq] += h
                            matrix1.values[ip][iq] = 0.0
                            for j in range(ip):
                                matrix1.__rotate(s, tau, j, ip, j, iq)
                            for j in range(ip + 1, iq):
                                matrix1.__rotate(s, tau, ip, j, j, iq)
                            for j in range(iq + 1, self.row):
                                matrix1.__rotate(s, tau, ip, j, iq, j)
                            for j in range(self.row):
                                v.__rotate(s, tau, j, ip, j, iq)
            for ip in range(self.row):
                b[ip] = b[ip] + z[ip]
                d[ip] = b[ip]
                z[ip] = 0.0
        result = []
        for i in range(self.row):
            if d[i] > 0:
                result.append(Eigenvector(d[i], v.getColumnVector(i)))
        result.sort(key=lambda eigenvector: eigenvector.eigenvalue, reverse=True)
        return result
