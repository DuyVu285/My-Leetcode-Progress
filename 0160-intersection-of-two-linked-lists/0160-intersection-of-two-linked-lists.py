# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None

        pointerA = headA
        pointerB = headB

        while pointerA != pointerB:
            if pointerA is None:
                pointerA = headB
            else:
                pointerA = pointerA.next

            if pointerB is None:
                pointerB = headA
            else:
                pointerB = pointerB.next

        return pointerA