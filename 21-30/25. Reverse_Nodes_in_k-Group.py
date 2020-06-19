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
    def reverse_linkList(self, head, rear):
        new_head = ListNode(0)
        new_rear = head

        while head != rear:
            tmp_point = head.next
            head.next = new_head.next
            new_head.next = head
            head = tmp_point
        head.next = new_head.next
        new_head.next = head
        return new_head.next, new_rear

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k <= 1: return head

        new_head = ListNode(0)
        new_head.next = head

        font = rear = new_head
        for i in range(k):
            if font != None: font = font.next
            else: return head

        while True:
            cur_font = font.next
            sub_font, sub_rear = self.reverse_linkList(rear.next, font)
            rear.next = sub_font
            sub_rear.next = cur_font
            font = sub_rear

            for i in range(k):
                if font.next != None:
                    font = font.next
                    rear = rear.next
                else: return new_head.next



if __name__ == '__main__':
    l = create_link([1, 2, 3, 4, 5])
    check_link(l)
    s = Solution()
    result = s.reverseKGroup(l, 3)
    check_link(result)



