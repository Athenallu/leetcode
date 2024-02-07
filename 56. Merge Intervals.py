class Solution:
    def merge(self, intervals):
        intervals.sort()
        res=[intervals[0]]
        for j in range(1, len(intervals)):
            if intervals[j][0]<=res[-1][1]:
                p=res.pop()
                res.append([p[0], max(intervals[j][1], p[1])])
            else:
                res.append(intervals[j])
        return res



        '''
        if len(intervals)==1:
            return intervals
        inter=sorted(intervals)
        inter=inter[::-1]
        ans=[]
        while inter:
            #if len(inter)==1:
            #    ans.append(inter.pop())
            if len(inter)>=2 and inter[-2][0]<=inter[-1][1]:
                tmp=[inter[-1][0], max(inter[-1][1], inter[-2][1])]
                inter.pop()
                inter.pop()
                inter.append(tmp)
            else:
                ans.append(inter.pop())
        return ans
        '''
            
