class MatrixDimensionMismatch(Exception):

    def __init__(self):
        self.message = "The number of rows and columns of the first matrix should be equal to the number of rows and columns of the second matrix respectively."
