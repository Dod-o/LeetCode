#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_link(nums):
    head = ListNode(None)
    cur_node = head

    for i in range(len(nums)):
        cur_node.next = ListNode(nums[i])
        cur_node = cur_node.next

    return head.next

def check_link(link):
    while link != None:
        print(link.val, end=' ')
        link = link.next
    print()

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        head = ListNode(0)
        cur_point = head
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                cur_point.next = l1
                cur_point = cur_point.next
                l1 = l1.next
            else:
                cur_point.next = l2
                cur_point = cur_point.next
                l2 = l2.next
        while l1 != None:
            cur_point.next = l1
            cur_point = cur_point.next
            l1 = l1.next
        while l2 != None:
            cur_point.next = l2
            cur_point = cur_point.next
            l2 = l2.next
        cur_point.next = None
        return head.next



if __name__ == '__main__':
    l1 = create_link([1, 2, 4])
    l2 = create_link([1, 3, 4])
    check_link(l1)
    check_link(l2)
    s = Solution()
    result = s.mergeTwoLists(l1, l2)
    check_link(result)