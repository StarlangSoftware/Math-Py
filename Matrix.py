import random
import Vector


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
    def __init__(self, row, col):
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
    def initRandom(self, minValue, maxValue):
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
    def getValue(self, rowNo, colNo):
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
    def setValue(self, rowNo, colNo, value):
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
    def addValue(self, rowNo, colNo, value):
        self.values[rowNo][colNo] += value

    """
     * The increment method adds 1 to the item at given index of values list.
     *
     * @param rowNo integer input for row number.
     * @param colNo integer input for column number.
    """
    def increment(self, rowNo, colNo):
        self.values[rowNo][colNo] += 1

    """
    The getter for the row variable.

    RETURNS
    -------
    int
        row number.
    """
    def getRow(self):
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
    def getRowVector(self, row):
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
    def getColumn(self):
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
    def getColumnVector(self, column):
        columnVector = Vector.Vector()
        for i in range(self.row):
            columnVector.add(self.values[i][column])
        return columnVector
