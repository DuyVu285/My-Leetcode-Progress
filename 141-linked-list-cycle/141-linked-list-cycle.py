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
        mark1 = head
        mark2 = head
        while mark2 != None and mark2.next != None:
            mark1 = mark1.next
            mark2 = mark2.next.next
            if mark2 == mark1:
                return True
        return False