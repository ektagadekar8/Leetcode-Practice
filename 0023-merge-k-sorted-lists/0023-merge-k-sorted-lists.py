class Solution(object):
    def mergeKLists(self, lists):
        if not lists:
            return None

        result = lists[0]

        for i in range(1, len(lists)):
            result = self.mergeTwoLists(result, lists[i])

        return result

    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        current = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next

            current = current.next

        if l1:
            current.next = l1
        else:
            current.next = l2

        return dummy.next