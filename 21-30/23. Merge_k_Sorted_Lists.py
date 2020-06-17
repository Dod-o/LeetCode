# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        nums = []
        for List in lists:
            while List != None:
                nums.append(List.val)
                List = List.next
        nums = sorted(nums)
        head = point = ListNode(0)
        for i in range(len(nums)):
            point.next = ListNode(nums[i])
            point = point.next
        return head.next



if __name__ == '__main__':
    pass