class Solution:
    def minCostClimbingStairs(self, cost: 'List[int]') -> 'int':
        l= len(cost)
        for i in range(2,l):
            cost[i]+=min(cost[i-1],cost[i-2])
        return min(cost[l-1], cost[l-2])
