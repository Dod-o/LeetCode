import copy

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

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
    def get_nums(self, link):
        result = 0
        multiple = 1
        while link != None:
            result += link.val * multiple
            multiple *= 10
            link = link.next
        return result

    def create_link(self, nums):
        link_nums = []
        if nums == 0: link_nums.append(0)
        else:
            while nums != 0:
                link_nums.append(nums % 10)
                nums //= 10

        head = ListNode(None)
        cur_node = head
        for i in range(len(link_nums)):
            cur_node.next = ListNode(link_nums[i])
            cur_node = cur_node.next
        return head.next

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = self.get_nums(l1)
        num2 = self.get_nums(l2)
        return self.create_link(num1 + num2)

if __name__ == '__main__':
    l1 = create_link([2, 4, 3])
    l2 = create_link([5, 6, 4])

    s = Solution()
    result = s.addTwoNumbers(l1, l2)
    check_link(result)
