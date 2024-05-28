from typing import List

class Solution:
    def solve(self, ind: int, cost: List[int], w: int, dp: List[List[int]]) -> int:
        if w == 0:
            return 0
        if ind >= len(cost) or ind + 1 > w:
            return 1e9
        
        if dp[ind][w] != -1:
            return dp[ind][w]
        
        a, b = float('inf'), float('inf')
        if cost[ind] != -1 and ind + 1 <= w:
            a = cost[ind] + self.solve(ind, cost, w - (ind + 1), dp)
        b = self.solve(ind + 1, cost, w, dp)
        
        dp[ind][w] = min(a, b)
        return dp[ind][w]

    def minimumCost(self, n: int, w: int, cost: List[int]) -> int:
        dp = [[-1] * (w + 1) for _ in range(n + 1)]
        ans = self.solve(0, cost, w, dp)
        
        if ans >= 1e9:
            ans = -1
        
        return ans
