class Solution:
    memo = {}
    def climbStairs(self, n: int) -> int:
        ''' if n <= 2:
            return n
        if n not in self.memo:
            self.memo[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)

        return self.memo[n] '''

        if n <= 2:
            return n
            
        prev1 = 1
        prev2 = 2

        for i in range(3, n + 1):
            current = prev1 + prev2

            prev1 = prev2
            prev2 = current
        
        return prev2