class Solution:
    def canJump(self, nums) -> bool:
        if len(nums)==1:
            return True
        cover=0
        i=0
        while i<=cover:
            cover=max(cover, i+nums[i])
            if cover>=len(nums)-1:
                return True
            i+=1
        return False


        '''
        if len(nums)==1:
            return True
        from collections import deque
        q=deque()
        q.append(0)
        while q:
            for i in range(len(q)):
                peek=q.popleft()
                if peek+nums[peek]>=len(nums)-1:
                    return True
                for j in range(peek+1, min(len(nums), peek+nums[peek]+1)):
                    if j+nums[j]>=len(nums)-1:
                        return True
                    q.append(j)
        return False


#        while q:
#            for i in range(len(q)):
#                peek=q.popleft()
#                for j in range(peek+1, min(peek+nums[peek]+1, len#(nums))):
#                    if j+nums[j]>=len(nums):
#                        return True
#                    q.append(j)
#        return False
'''