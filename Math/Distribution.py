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

    @staticmethod
    def __ex(x: float) -> float:
        """
        The ex method takes a double x as an input, if x is less than -BIGX it returns 0, otherwise it returns Euler's
        number e raised to the power of x.

        PARAMETERS
        ----------
        x : double
            double input.

        RETURNS
        -------
        double
            0 if input is less than -BIGX, Euler's number e raised to the power of x otherwise.
        """
        if x < -Distribution.BIGX:
            return 0
        return math.exp(x)

    @staticmethod
    def beta(x: list) -> float:
        """
        The beta method takes a double list x as an input. It loops through x and accumulates
        the value of gammaLn(x), also it sums up the items of x and returns (accumulated result - gammaLn of this
        summation).

        PARAMETERS
        ----------
        x : list
            double list input.

        RETURNS
        -------
        double
            beta distribution at point x.
        """
        total = 0.0
        result = 0.0
        for i in range(len(x)):
            result += Distribution.gammaLn(x[i])
            total += x[i]
        result -= Distribution.gammaLn(total)
        return result

    @staticmethod
    def gammaLn(x: float) -> float:
        """
        The gammaLn method takes a double x as an input and returns the logarithmic result of the gamma distribution at
        point x.

        PARAMETERS
        ----------
        x : double
            double input.

        RETURNS
        -------
        double
            the logarithmic result of the gamma distribution at point x.
        """
        cof = [76.18009172947146, -86.50532032941677, 24.01409824083091, -1.231739572450155, 0.1208650973866179e-2,
               -0.5395239384953e-5]
        y = x
        tmp = x + 5.5
        tmp -= (x + 0.5) * math.log(tmp)
        ser = 1.000000000190015
        for j in range(6):
            y = y + 1
            ser += cof[j] / y
        return -tmp + math.log(2.5066282746310005 * ser / x)

    @staticmethod
    def zNormal(z: float) -> float:
        """
        The zNormal method performs the Z-Normalization. It ensures, that all elements of the input vector are
        transformed into the output vector whose mean is approximately 0 while the standard deviation is in a range
        close to 1.

        PARAMETERS
        ----------
        z : double
            double input.

        RETURNS
        -------
        double
            normalized value of given input.
        """
        if z == 0.0:
            x = 0.0
        else:
            y = 0.5 * abs(z)
            if y >= Distribution.Z_MAX * 0.5:
                x = 1.0
            else:
                if y < 1.0:
                    w = y * y
                    x = ((((((((0.000124818987 * w - 0.001075204047) * w + 0.005198775019) * w - 0.019198292004) * w
                             + 0.059054035642) * w - 0.151968751364) * w + 0.319152932694) * w - 0.531923007300) * w
                         + 0.797884560593) * y * 2.0
                else:
                    y -= 2.0
                    x = (((((((((((((-0.000045255659 * y + 0.000152529290) * y - 0.000019538132) * y
                                   - 0.000676904986) * y + 0.001390604284) * y - 0.000794620820) * y
                                - 0.002034254874) * y + 0.006549791214) * y - 0.010557625006) * y + 0.011630447319) * y
                            - 0.009279453341) * y + 0.005353579108) * y - 0.002141268741) * y + 0.000535310849) * y \
                        + 0.999936657524
        if z > 0.0:
            return (x + 1.0) * 0.5
        else:
            return (1.0 - x) * 0.5

    @staticmethod
    def zInverse(p: float) -> float:
        """
        The zInverse method returns the Z-Inverse of given probability value.

        PARAMETERS
        ----------
        p : double
            probability input.

        RETURNS
        -------
        double
            the Z-Inverse of given probability.
        """
        minz = -Distribution.Z_MAX
        maxz = Distribution.Z_MAX
        zval = 0.0
        if p <= 0.0 or p >= 1.0:
            return 0.0
        while maxz - minz > Distribution.Z_EPSILON:
            pval = Distribution.zNormal(zval)
            if pval > p:
                maxz = zval
            else:
                minz = zval
            zval = (maxz + minz) * 0.5
        return zval

    @staticmethod
    def chiSquare(x: float, freedom: int) -> float:
        """
        The chiSquare method is used to determine whether there is a significant difference between the expected
        frequencies and the observed frequencies in one or more categories. It takes a double input x and an integer
        freedom for degrees of freedom as inputs. It returns the Chi Squared result.

        PARAMETERS
        ----------
        x : double
            double input.
        freedom : int
            integer input for degrees of freedom.

        RETURNS
        -------
        double
            the Chi Squared result.
        """
        y = 0
        if x <= 0.0 or freedom < 1:
            return 1.0
        a = 0.5 * x
        even = (freedom % 2 == 0)
        if freedom > 1:
            y = Distribution.__ex(-a)
        if even:
            s = y
        else:
            s = 2.0 * Distribution.zNormal(-math.sqrt(x))
        if freedom > 2:
            x = 0.5 * (freedom - 1.0)
            if even:
                z = 1.0
            else:
                z = 0.5
            if a > Distribution.BIGX:
                if even:
                    e = 0.0
                else:
                    e = Distribution.LOG_SQRT_PI
                c = math.log(a)
                while z <= x:
                    e = math.log(z) + e
                    s += Distribution.__ex(c * z - a - e)
                    z += 1.0
                return s
            else:
                if even:
                    e = 1.0
                else:
                    e = Distribution.I_SQRT_PI / math.sqrt(a)
                c = 0.0
                while z <= x:
                    e = e * (a / z)
                    c = c + e
                    z += 1.0
                return c * y + s
        else:
            return s

    @staticmethod
    def chiSquareInverse(p: float, freedom: int) -> float:
        """
        The chiSquareInverse method returns the Chi Square-Inverse of given probability value with given degree of
        freedom.

        PARAMETERS
        ----------
        p : double
            probability input.
        freedom : int
            integer input for degrees of freedom.

        RETURNS
        -------
        double
            the chiSquare-Inverse of given probability.
        """
        minchisq = 0.0
        maxchisq = Distribution.CHI_MAX
        if p <= 0.0:
            return maxchisq
        else:
            if p >= 1.0:
                return 0.0
        chisqval = freedom / math.sqrt(p)
        while maxchisq - minchisq > Distribution.CHI_EPSILON:
            if Distribution.chiSquare(chisqval, freedom) < p:
                maxchisq = chisqval
            else:
                minchisq = chisqval
            chisqval = (maxchisq + minchisq) * 0.5
        return chisqval

    @staticmethod
    def fDistribution(F: float, freedom1: int, freedom2: int) -> float:
        """
        The fDistribution method is used to observe whether two samples have the same variance. It takes a double input
        F and two integer freedom1 and freedom2 for degrees of freedom as inputs. It returns the F-Distribution result.

        PARAMETERS
        ----------
        F : double
            double input.
        freedom1 : int
            integer input for degrees of freedom.
        freedom2 : int
            integer input for degrees of freedom.

        RETURNS
        -------
        double
            the F-Distribution result.
        """
        if F < Distribution.F_EPSILON or freedom1 < 1 or freedom2 < 1:
            return 1.0
        if freedom1 % 2 != 0:
            a = 1
        else:
            a = 2
        if freedom2 % 2 != 0:
            b = 1
        else:
            b = 2
        w = (F * freedom1) / freedom2
        z = 1.0 / (1.0 + w)
        if a == 1:
            if b == 1:
                p = math.sqrt(w)
                y = Distribution.I_PI
                d = y * z / p
                p = 2.0 * y * math.atan(p)
            else:
                p = math.sqrt(w * z)
                d = 0.5 * p * z / w
        else:
            if b == 1:
                p = math.sqrt(z)
                d = 0.5 * z * p
                p = 1.0 - p
            else:
                d = z * z
                p = w * z
        y = 2.0 * w / z
        for j in range(b + 2, freedom2 + 1, 2):
            d *= (1.0 + a / (j - 2.0)) * z
            if a == 1:
                p = p + d * y / (j - 1.0)
            else:
                p = (p + w) * z
        y = w * z
        z = 2.0 / z
        b = freedom2 - 2
        for i in range(a + 2, freedom1 + 1, 2):
            j = i + b
            d *= y * j / (i - 2.0)
            p -= z * d / j
        if p < 0.0:
            p = 0.0
        else:
            if p > 1.0:
                p = 1.0
        return 1.0 - p

    @staticmethod
    def fDistributionInverse(p: float, freedom1: int, freedom2: int) -> float:
        """
        The fDistributionInverse method returns the F-Distribution Inverse of given probability value.

        PARAMETERS
        ----------
        p : double
            double probability.
        freedom1 : int
            integer input for degrees of freedom.
        freedom2 : int
            integer input for degrees of freedom.

        RETURNS
        -------
        double
            the F-Distribution Inverse of given probability.
        """
        maxf = Distribution.F_MAX
        minf = 0.0
        if p <= 0.0 or p >= 1.0:
            return 0.0
        if freedom1 == freedom2 and freedom1 > 2500:
            return 1 + 4.0 / freedom1
        fval = 1.0 / p
        while abs(maxf - minf) > Distribution.F_EPSILON:
            if Distribution.fDistribution(fval, freedom1, freedom2) < p:
                maxf = fval
            else:
                minf = fval
            fval = (maxf + minf) * 0.5
        return fval

    @staticmethod
    def tDistribution(T: float, freedom: int) -> float:
        """
        The tDistribution method is used instead of the normal distribution when there is small samples. It takes a
        double input T and an integer freedom for degree of freedom as inputs. It returns the T-Distribution result by
        using F-Distribution method.

        PARAMETERS
        ----------
        T : double
            double input.
        freedom : int
            integer input for degrees of freedom.

        RETURNS
        -------
        double
            the T-Distribution result.
        """
        if T >= 0:
            return Distribution.fDistribution(T * T, 1, freedom) / 2
        else:
            return 1 - Distribution.fDistribution(T * T, 1, freedom) / 2

    @staticmethod
    def tDistributionInverse(p: float, freedom: int) -> float:
        """
        The tDistributionInverse method returns the T-Distribution Inverse of given probability value.

        PARAMETERS
        ----------
        p : double
            double probability.
        freedom : int
            integer input for degrees of freedom.

        RETURNS
        -------
        double
            the T-Distribution Inverse of given probability.
        """
        if p < 0.5:
            return math.sqrt(Distribution.fDistributionInverse(p * 2, 1, freedom))
        else:
            return -math.sqrt(Distribution.fDistributionInverse((1 - p) * 2, 1, freedom))
