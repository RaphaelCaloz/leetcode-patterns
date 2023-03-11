from math import sqrt

# Get all divisors of a number, in O( sqrt(num) ) time complexity.
class Solution:
    def get_divisors(self, num):
            divisors = []
            for i in range(1, int(sqrt(num))+1):
                if num % i == 0:
                    divisors.append(i)
                    divisors.append(num//i)
            return list(set(divisors))  # Eliminate duplicates