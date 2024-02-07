class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict, deque
        dic=defaultdict(list)
        incoming=[0]*numCourses
        for pair in prerequisites:
            dic[pair[1]].append(pair[0])
            incoming[pair[0]]+=1
        q=deque()
        for i in range(numCourses):
            if incoming[i]==0:
                q.append(i)
        l=[]
        while q:
            peek=q.popleft()
            l.append(peek)
            for nb in dic[peek]:
                incoming[nb]-=1
                if incoming[nb]==0:
                    q.append(nb)
        if len(l)==numCourses:
            return True
        else:
            return False