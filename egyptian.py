"""
Egyptian algorithm
"""

def egyptian_multiplication(a, n):
    """
    returns the product a * n

    assume n is a nonegative integer
    """
    def isodd(n):
        """
        returns True if n is odd
        """
        return n & 0x1 == 1

    if n == 1:
        return a
    if n == 0:
        return 0

    if isodd(n):
        return egyptian_multiplication(a + a, n // 2) + a
    else:
        return egyptian_multiplication(a + a, n // 2)


if __name__ == '__main__':
    # this code runs when executed as a script
    for a in [1,2,3]:
        for n in [1,2,5,10]:
            print("{} * {} = {}".format(a, n, egyptian_multiplication(a,n)))


#Egyptian algorithm
#floor(log2(n))+#n-1

def power(a, n):
    def isodd(n):
        return n & 0x1 == 1

    if n == 1:
        return a
    if n == 0:
        return 0

    if isodd(n):
        return power(a * a, n // 2) * a
    else:
        return power(a * a, n // 2)

power(4,3)

    computes the power a ** n

    assume n is a nonegative integer
    """
    pass
