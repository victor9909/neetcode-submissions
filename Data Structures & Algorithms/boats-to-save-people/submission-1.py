class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        # [5,1,4,2] limit = 6
        # [1, 2, 4, 5]
        # 1,5
        # 2,4

        # [1,3,2,3,2] limit = 3
        # [1, 2, 2, 3, 3]
        # 3
        # 3
        # [1, 2]
        # 2

        people.sort()

        res, l, r = 0, 0, len(people) - 1
        while l <= r:
            weight = people[r] + people[l]
            if weight <= limit:
                l += 1
            res += 1
            r -= 1
            
        return res
