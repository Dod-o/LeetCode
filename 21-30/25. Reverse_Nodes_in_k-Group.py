class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        nodeList = []
        p = head
        while p != None:
            nodeList.append(p)
            p = p.next

        if len(nodeList) < k:
            return head

        nodeList[-1].next = nodeList[0]

        for i in range(len(nodeList)):
            if (i + 1) % k == 0:
                left = i - (k - 1)
                right = i
                while left < right:
                    tmp = nodeList[left]
                    nodeList[left] = nodeList[right]
                    nodeList[right] = tmp
                    nodeList[left - 1].next = nodeList[left]
                    nodeList[left].next = nodeList[left + 1]
                    nodeList[right - 1].next = nodeList[right]
                    nodeList[right].next = nodeList[(right + 1) % len(nodeList)]
                    left += 1
                    right -= 1


        nodeList[-1].next = None
        return nodeList[0]