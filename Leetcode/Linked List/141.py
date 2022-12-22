# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        seen = []
        current = head
        while current:
            seen.append(current)
            current = current.next
            if current in seen:
                return True
        return False