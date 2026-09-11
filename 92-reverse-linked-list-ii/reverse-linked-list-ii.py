class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        current = head

        # Reach the node at position left
        for _ in range(left - 1):
            prev = current
            current = current.next

        # Remember the first node of the section being reversed
        left_node = current
        reverse_prev = None

        # Reverse left → right
        for _ in range(right - left + 1):
            nextt = current.next
            current.next = reverse_prev
            reverse_prev = current
            current = nextt

        # Reconnect
        prev.next = reverse_prev
        left_node.next = current

        return dummy.next