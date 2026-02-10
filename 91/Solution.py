class Solution:
    def numDecodings(self, s: str) -> int:

        n = len(s)
        dp = [[0]*2 for _ in range(n)]

        if n == 0:
            return 0

        if s[0] == '0':
            return 0
        
        dp[0][0] = 1
        dp[0][1] = 0

        for i in range(1,n,1):

            if s[i] == '0':
                dp[i][0] = 0
            else:
                dp[i][0] = dp[i-1][0] + dp[i-1][1]
            
            if int(s[i-1])*10 + int(s[i]) <= 26:
                dp[i][1] = dp[i-1][0]
            
            if sum(dp[i]) == 0:
                return 0
        return sum(dp[n-1])

# https://leetcode.com/problems/decode-ways/
# Medium, Dynamic Programming
# Tags: Dynamic Programming, String
# Difficulty: Medium