class Solution:
    def numDecodings(self, s: str) -> int:
        
        map_digit = {
            "1": "A",
            "2": "B",
            "3": "C",
            "4": "D",
            "5": "E",
            "6": "F",
            "7": "G",
            "8": "H",
            "9": "I",
            "10": "J",
            "11": "K",
            "12": "L",
            "13": "M",
            "14": "N",
            "15": "O",
            "16": "P",
            "17": "Q",
            "18": "R",
            "19": "S",
            "20": "T",
            "21": "U",
            "22": "V",
            "23": "W",
            "24": "X",
            "25": "Y",
            "26": "Z"
        }
        res = 0
        memo = {len(s): 1}

        def dpf(i):
            
            if i in memo:
                return memo[i]

            if i >= len(s):
                return 1
            
            res = 0
            for j in range(i, i+2):
                if j >= len(s):
                    continue
                if s[i:j+1] in map_digit:
                    res += dpf(j + 1)
            memo[i] = res
            return memo[i]
        
        dp = [0] * (len(s) + 1)
        dp[-1] = 1

        for i in range(len(s) - 1, -1, -1):
            for j in range(i, i+2):
                if j >= len(s):
                    continue
                if s[i:j+1] in map_digit:
                    dp[i] += dp[j + 1]
        return dp[0]
        
        #return dp(0)

