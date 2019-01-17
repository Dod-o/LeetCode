class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        linkList = []
        point = head
        while point != None:
            linkList.append(point)
            point = point.next
        index = len(linkList) - n
        if index == 0:
            return linkList[0].next
        else:
            linkList[index - 1].next = linkList[index].next
        return linkList[0]