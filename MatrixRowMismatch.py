class MatrixRowMismatch(Exception):

    def __init__(self):
        self.message = "Number of rows of the matrix should be equal to the size of the vector."
