import math
def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

def climbStairs(n):
    """
    :type n: int
    :rtype: int
    ex) num_stairs(6) = 6C0 + 5C1 + 4C2 + 3C3
    each iteration, count all combinations of solution with r number of 2s 
    """
    r = 0
    num_stairs = 0
    while (n >= r):
        num_stairs += nCr(n,r)
        n -= 1
        r += 1

    return num_stairs