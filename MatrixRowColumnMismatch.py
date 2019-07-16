class MatrixRowColumnMismatch(Exception):

    def __init__(self):
        self.message = "The number of columns of the first matrix should be equal to the number of rows of the second matrix."
