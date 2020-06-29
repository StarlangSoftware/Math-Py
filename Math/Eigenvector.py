from Math.Vector import Vector


class Eigenvector(Vector):

    eigenvalue: float

    def __init__(self, eigenvalue: float, values: list):
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
        super().__init__(values)
        self.eigenvalue = eigenvalue

    def getEigenvalue(self) -> float:
        """
        The eigenValue method which returns the eigenValue variable.

        RETURNS
        -------
        double
            eigenValue variable.
        """
        return self.eigenvalue
