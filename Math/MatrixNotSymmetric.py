class MatrixNotSymmetric(Exception):

    def __init__(self):
        self.message = "Matrix should be symmetric."
