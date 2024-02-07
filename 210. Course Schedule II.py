class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        from collections import deque
        AL=[[] for i in range(numCourses)]
        incoming=[0]*numCourses
        for pair in prerequisites:
            AL[pair[1]].append(pair[0])
            incoming[pair[0]]+=1
        q=deque()
        for i in range(numCourses):
            if incoming[i]==0:
                q.append(i)
        res=[]
        while q:
            peek=q.popleft()
            res.append(peek)
            for nb in AL[peek]:
                incoming[nb]-=1
                if incoming[nb]==0:
                    q.append(nb)
        if len(res)==numCourses:
            return res
        else:
            return []
