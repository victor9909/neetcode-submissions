class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        # [1,2,3,4]
        # [2,2,4,1]

        if sum(gas) < sum(cost):
            return -1
        
        curr, res = 0, 0

        for i in range(len(gas)):
            curr += gas[i] - cost[i]

            if curr < 0:
                curr = 0
                res = i + 1
            
        return res


