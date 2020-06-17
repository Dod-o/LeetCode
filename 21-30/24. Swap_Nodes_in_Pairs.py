# Definition for singly-linked list.
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
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None: return None
        if head.next == None: return head
        if head.next.next == None:
            new_head = head.next
            new_head.next = head
            new_head.next.next = None
            return new_head


        new_head = ListNode(0)
        new_head.next = head

        font_point = rear_point = new_head
        for i in range(3): font_point = font_point.next
        while font_point != None:
            tmp = rear_point.next
            rear_point.next = rear_point.next.next
            rear_point.next.next = tmp
            tmp.next = font_point

            rear_point = rear_point.next.next
            if font_point.next != None:
                if font_point.next.next != None:
                    font_point = font_point.next.next
                else:
                    rear_point.next = rear_point.next.next
                    rear_point.next.next = font_point
                    font_point.next = None
                    return new_head.next
            else:
                return new_head.next




if __name__ == '__main__':
    l = create_link([1, 2, 3, 4])
    s = Solution()
    result = s.swapPairs(l)
    check_link(result)