class Solution:

    def createList(self, list):
        if len(list) == 0:
            return None

        L = ListNode(list[0])
        Lc = L

        for i in range(1, len(list)):
            Lc.next = ListNode(list[i])
            Lc = Lc.next
        return L

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return []

        val = []
        for i in range(len(lists)):
            list = lists[i]
            while list != None:
                val.append(list.val)
                list = list.next

        val = sorted(val)
        print(val)
        val = self.createList(val)

        return val