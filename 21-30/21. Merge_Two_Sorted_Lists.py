# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None and l2 == None: return None

        if l1 == None and l2 != None: return l2
        elif l1 != None and l2 == None:  return l1

        if l1.val < l2.val:
            returnL = ListNode(l1.val)
            l1 = l1.next
        else:
            returnL = ListNode(l2.val)
            l2 = l2.next

        L = returnL
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                L.next = ListNode(l1.val)
                l1 = l1.next
            else:
                L.next = ListNode(l2.val)
                l2 = l2.next
            L = L.next

        while l1 != None:
            L.next = ListNode(l1.val)
            l1 = l1.next
            L = L.next
        while l2 != None:
            L.next = ListNode(l2.val)
            l2 = l2.next
            L = L.next

        return returnL
