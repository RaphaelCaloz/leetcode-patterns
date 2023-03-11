"""
Calculate the Greatest Common Divisor of a and b using the euclidean algorithm.

Unless b==0, the result will have the same sign as b (so that when
b is divided by it, the result comes out positive).
"""
def gcd(a, b):
    while b:
        a, b = b, a%b
    return a