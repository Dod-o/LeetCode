# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        point = l1
        n1 = 0
        index = 0
        while point != None:
            n1 = n1 + point.val * (10 ** index)
            index += 1
            point = point.next
        point = l2
        n2 = 0
        index = 0
        while point != None:
            n2 = n2 + point.val * (10 ** index)
            index += 1
            point = point.next

        sum = n1 + n2
        if sum == 0:
            l = ListNode(0)
            return l
        else:
            point = ListNode(sum % 10)
            sum = sum // 10
            head = point
        while sum != 0:
            point.next = ListNode(sum % 10)
            point = point.next
            sum = sum // 10
        return head


s = Solution()
a = ListNode(1)
b = ListNode(8)
a.next = b

c = ListNode(0)
# d = ListNode(4)
# c.next = d

s = Solution()
x = s.addTwoNumbers(a, c)
print(x.val, x.next.val)