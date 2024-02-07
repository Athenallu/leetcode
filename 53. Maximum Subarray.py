class Solution:
    def maxSubArray(self, nums) -> int:
        res = nums[0]   # keep the maximum sum
        cur_sum=nums[0]
        i=1
        while i<len(nums):
            if cur_sum<=0:
                cur_sum=nums[i]
            else:
                cur_sum+=nums[i]
            res=max(res, cur_sum)
            i+=1
        return res

