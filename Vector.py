class Vector(object):

    """
    A constructor of Vector class which takes a list values as an input. Then, initializes
    values list and size variable with given input and its size.

    Parameters
    ----------
    values : list
        list input.
    """
    def __init__(self, values):
        self.values = values
        self.size = len(values)

    """
    Another constructor of Vector class which takes integer size and double x as inputs. Then, initializes size
    variable with given size input and creates new values list and adds given input x to values list.

    Parameters
    ----------
    size : int
        list size.
    x : double   
        item to add values list.
    """
    def allSame(self, size, x):
        self.size = size
        values = []
        for i in range(size):
            values.append(x)
