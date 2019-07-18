class Eigenvector(object):

    """
    A constructor of Eigenvector which takes a double eigenValue and an list values as inputs.
    It calls its super class Vector with values list and initializes eigenValue variable with its
    eigenValue input.

    Parameters
    ----------
    eigenvalue : double
        eigenValue double input.
    values : list
        list input.
    """
    def __init__(self, eigenvalue, values):
        super(values)
        self.eigenvalue = eigenvalue

    """
    The eigenValue method which returns the eigenValue variable.
    Returns
    -------
    double
        eigenValue variable.
    """
    def eigenValue(self):
        return self.eigenvalue
