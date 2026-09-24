class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        

        def find_peak():

            l, r = 0, mountainArr.length() - 2

            while l <= r:

                m = l + (r - l) // 2

                if mountainArr.get(m) < mountainArr.get(m + 1):
                    l = m + 1
                else:
                    r = m - 1
            
            return l
        
        peak = find_peak()
        
        def find_left():

            l, r = 0, peak

            while l <= r:

                m = l + (r - l) // 2
                item = mountainArr.get(m)
                if item == target:
                    return m
                elif item < target:
                    l = m + 1
                else:
                    r = m - 1
            
            return -1
        
        def find_right():

            l, r = peak + 1, mountainArr.length() - 1

            while l <= r:

                m = l + (r - l) // 2
                item = mountainArr.get(m)
                if item == target:
                    return m
                elif item > target:
                    l = m + 1
                else:
                    r = m - 1
            
            return -1

        first = find_left()
        if first != - 1:
            return first
        else:
            return find_right()
        

