class Solution:
    def numTrees(self, n: int) -> int:
        if n==0 or n==1:
            return 1
        if n==2:
            return 2
        dp=[0]*(n+1)
        dp[0]=1
        dp[1]=1
        dp[2]=2

        for i in range(3,n+1):
            for root in range(1,i+1):
                leftnum=root-1
                rightnum=i-root
                dp[i]+=dp[leftnum]*dp[rightnum]
        
        return dp[n]
