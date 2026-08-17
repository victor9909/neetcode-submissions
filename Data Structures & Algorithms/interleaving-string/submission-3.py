class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        dp = {}

        def dfs(i, j, k):
            
            if (i, j, k) in dp:
                return dp[(i, j, k)]

            if k == len(s3):
                return (i == len(s1)) and (j == len(s2))

            if i < len(s1) and s1[i] == s3[k]:
                dp[(i, j, k)] = dfs(i + 1, j, k + 1)
                if dp[(i, j, k)]:
                    return True

            if j < len(s2) and s2[j] == s3[k]:
                dp[(i, j, k)] = dfs(i, j + 1, k + 1)
                if dp[(i, j, k)]:
                    return True

            return False

        #return dfs(0, 0, 0)


        def dp():

            if len(s1) + len(s2) != len(s3):
                return False

            dp = {}

            for i in range(len(s1), -1, -1):
                for j in range(len(s2), -1, -1):
                    if i == len(s1) and j == len(s2):
                        dp[(i, j)] = True
                        continue

                    k = i + j
                    ans = False

                    if i < len(s1) and s1[i] == s3[k]:
                        ans |= dp.get((i + 1, j), False)

                    if j < len(s2) and s2[j] == s3[k]:
                        ans |= dp.get((i, j + 1), False)

                    dp[(i, j)] = ans

            return dp[(0, 0)]

        return dp()

