class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people.sort()
        l, r = 0, len(people) - 1
        res = 0
        curr_w = 0
        while l <= r:
            curr_w += people[l] + people[r]
            if curr_w == limit:
                res += 1
                l, r = l + 1, r - 1
                curr_w = 0
            elif curr_w > limit:
                res += 1
                r -= 1
                curr_w = 0
            else:
                if l == r:
                    res += 1
                l += 1
            
        return res