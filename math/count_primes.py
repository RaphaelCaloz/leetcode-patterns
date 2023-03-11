# Count the number of prime number strictly inferior
# to n. This is an implementation of the sieve of
# Eratosthenes algorithm.
# Time complexity: O(n log(log(n))) 
# => more efficient than O(n) for values under 10^10
# Space complexity: O(n)
class Solution:
    def countPrimes(self, n: int) -> int:
        seen, ans = [False] * n, 0
        for num in range(2, n):
            if seen[num]: continue
            ans += 1
            for i in range(num*num, n, num):
                seen[i] = True
        return ans  