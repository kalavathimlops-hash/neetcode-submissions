class Solution:
    def reverseList(self,head:ListNode)->ListNode:
        prev,curr=none,head
        while curr:
            temp=curr.next
            curr.next=prev
            curr=prev
            curr=temp
        return prev    