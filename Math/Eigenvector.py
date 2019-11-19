from Math.Vector import Vector


class Eigenvector(Vector):

    __eigenvalue: float

    """
    A constructor of Eigenvector which takes a double eigenValue and an list values as inputs.
    It calls its super class Vector with values list and initializes eigenValue variable with its
    eigenValue input.

    PARAMETERS
    ----------
    eigenvalue : double
        eigenValue double input.
    values : list
        list input.
    """
    def __init__(self, eigenvalue: float, values: list):
        super().__init__(values)
        self.__eigenvalue = eigenvalue

    """
    The eigenValue method which returns the eigenValue variable.

    RETURNS
    -------
    double
        eigenValue variable.
    """
    def eigenValue(self) -> float:
        return self.__eigenvalue
