class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        memo = {}

        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if j == n:
                return i == m

            match = i < m and (s[i] == p[j] or p[j] == ".")
            if (j + 1) < n and p[j + 1] == "*":
                memo[(i, j)] = (dfs(i, j + 2) or          # don't use *
                       (match and dfs(i + 1, j))) # use *
                return memo[(i, j)]
            if match:
                memo[(i, j)] = dfs(i + 1, j + 1)
                return memo[(i, j)]
            return False

        return dfs(0, 0)