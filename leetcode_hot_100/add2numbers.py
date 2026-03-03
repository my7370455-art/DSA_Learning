class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        output = 0
        node1 = l1
        node2 = l2
        while node1 or node2:
            count += 1
            if node1:
                output += node1.val * (10 ** (count - 1))
                node1 = node1.next
            if node2:
                output += node2.val * (10 ** (count - 1))
                node2 = node2.next


        output = str(output)[::-1]
        head = ListNode(int(output[0]))
        node = head
        for i in range(1, len(output)):
            node.next = ListNode(int(output[i]))
            node = node.next

        return head