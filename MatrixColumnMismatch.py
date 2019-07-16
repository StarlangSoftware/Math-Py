class MatrixColumnMismatch(Exception):

    def __init__(self):
        self.message = "Number of columns of the matrix should be equal to the size of the vector."
