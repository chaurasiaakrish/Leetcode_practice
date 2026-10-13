# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        dummy=ListNode()
        prev=dummy
        curr1=list1
        curr2=list2

        while curr1 is not None and curr2 is not None:
            if curr1.val<=curr2.val:
                prev.next=curr1
                curr1=curr1.next
                prev=prev.next
            else:
                prev.next=curr2
                curr2=curr2.next
                prev=prev.next
        while curr1 is not None:
            prev.next=curr1
            curr1=curr1.next
            prev=prev.next
        while curr2 is not None:
            prev.next=curr2
            curr2=curr2.next
            prev=prev.next
        return dummy.next