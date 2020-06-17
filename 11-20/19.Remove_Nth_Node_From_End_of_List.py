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
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        front = head
        for i in range(1, n + 1):
            front = front.next
        if front == None: return head.next
        # if front.next == None: return head.next

        rear = head
        while front.next != None:
            front = front.next
            rear = rear.next
        if rear.next != None:
            rear.next = rear.next.next
        else:
            rear.next = None

        return head



if __name__ == '__main__':
    s = Solution()
    linked_list = create_link([1, 2])
    check_link(linked_list)
    result = s.removeNthFromEnd(linked_list, 2)
    check_link(result)