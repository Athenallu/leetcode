# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        dummyhead=ListNode(next=head)
        cnt=dummyhead
        len_list=0
        while cnt.next:
            len_list+=1
            cnt=cnt.next
        slow=dummyhead
        fast=head
        m=k%len_list
        if m==0:
            return head
        while fast.next and m>1:
            fast=fast.next
            m-=1
        while fast.next:
            fast=fast.next
            slow=slow.next
        newhead=slow.next
        slow.next=None
        if fast!=head:
            fast.next=head
        return newhead




        '''
        if not head:
            return None
        dummyhead=ListNode(next=head)
        slow=dummyhead
        fast=head
        for _ in range(k):
            if fast:
                fast=fast.next
        while fast:
            fast=fast.next
            slow=slow.next
        newtail=slow
        newhead=newtail.next
        newhead.next=head
        newtail.next=None
        return newhead
'''