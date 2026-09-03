class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n > 0:
            return Solution.powHelper(x, n)
        else:
            return 1.0 / Solution.powHelper(x, -n)

    @staticmethod
    def powHelper(x, n):
        result = 1.0

        while n > 0:
            if n & 1:
                result *= x
            
            x *= x

            n >>= 1

        return result
