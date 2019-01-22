class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        elif head.next == None:
            return head
        L = head
        newHead = L.next
        L.next = newHead.next
        newHead.next = L

        forePoint = newHead
        point = L
        index = 1
        while point != None:
            if index % 2 == 0:
                if point.next != None:
                    post = point.next

                    point.next = post.next
                    post.next = point
                    forePoint.next = post

                    forePoint = post
                index += 1

            else:
                forePoint = point
                point = point.next
                index += 1

        return newHead