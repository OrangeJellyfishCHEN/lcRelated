class LC2095(object):
    def deleteMiddle(self, head):
        if head.next is None:
            return None
        fast = slow = head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        prev.next = prev.next.next
        return head