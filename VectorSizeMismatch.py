class VectorSizeMismatch(Exception):

    def __init__(self):
        self.message = "Number of items in both vectors must be the same"
