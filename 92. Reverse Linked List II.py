# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head, left: int, right: int):
        if not head or left==right:
            return head
        dummyhead=ListNode(next=head)
        pre=dummyhead
        cur=dummyhead
        for _ in range(left):
            temp_1=pre
            pre=pre.next
            cur=cur.next
        temp_2=pre
        cur=cur.next
        for _ in range(right-left):
            tmp=cur.next
            cur.next=pre
            pre,cur=cur,tmp
        temp_1.next=pre
        temp_2.next=cur
        return dummyhead.next


        '''
        dummyhead=ListNode()
        dummyhead.next=head
        leftnode=head

        pre=leftnode
        tmp=leftnode

        for _ in range(1,left):
            pre=leftnode
            leftnode=leftnode.next
        oldleft=leftnode
        cur=leftnode
        next=cur.next
        for _ in range(left,right):
            if next.next:
                tmp=next.next
            next.next=cur
            cur,next=next,tmp
        pre.next=cur
        oldleft.next=tmp
        return dummyhead.next
        '''
            

        