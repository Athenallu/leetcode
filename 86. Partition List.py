# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head, x: int):
        if not head:
            return head
        small=[]
        large=[]
        cur=head
        while cur:
            if cur.val<x:
                small.append(cur)
            else:
                large.append(cur)
            cur=cur.next
        for i in range(len(small)-1):
            small[i].next=small[i+1]
        if small and large:
            small[-1].next=large[0]
        for i in range(len(large)-1):
            large[i].next=large[i+1]
        if large:
            large[-1].next=None
        if small:
            return small[0]
        else:
            return large[0]