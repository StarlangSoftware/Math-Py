import math


class Distribution(object):
    Z_MAX = 6.0
    Z_EPSILON = 0.000001
    CHI_EPSILON = 0.000001
    CHI_MAX = 99999.0
    LOG_SQRT_PI = 0.5723649429247000870717135
    I_SQRT_PI = 0.5641895835477562869480795
    BIGX = 200.0
    I_PI = 0.3183098861837906715377675
    F_EPSILON = 0.000001
    F_MAX = 9999.0

    """
    The ex method takes a double x as an input, if x is less than -BIGX it returns 0, otherwise it returns Euler's number
    e raised to the power of x.

    PARAMETERS
    ----------
    x : double
        double input.
        
    RETURNS
    -------
    int
        0 if input is less than -BIGX, Euler's number e raised to the power of x otherwise.
    """
    @staticmethod
    def ex(x):
        if x < -Distribution.BIGX:
            return 0
        return math.exp(x)
