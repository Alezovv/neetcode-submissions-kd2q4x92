class Solution:
    def myPow(self, x: float, n: int) -> float:
        a = x
        if n == 0:
            return 1

        for i in range(abs(n) - 1):
            a *= x
        print(a)
        if n < 0:
            return 1 / a

        return a