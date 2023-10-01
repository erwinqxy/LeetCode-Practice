class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        table = [0] * (n+1) 
        
        for i in range (2, n+1):
            take_one_step = table[i - 1] + cost[i - 1]
            take_two_steps = table[i - 2] + cost[i - 2]
            table[i] = min(take_one_step, take_two_steps)
        
        return table[-1]