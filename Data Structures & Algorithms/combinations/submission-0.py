class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        arr = [i for i in range(1, n + 1, 1)]
        
        res = []
        visit = set()

        def dfs(curr, idx):
            if len(curr) == k:
                res.append(curr[:])
                visit.add(tuple(curr[:]))
            if idx > len(arr) - 1 or tuple(curr[:]) in visit:
                return

            curr.append(arr[idx])
            dfs(curr, idx + 1)
            curr.pop()
            dfs(curr, idx + 1)

        dfs([], 0)
        return res

