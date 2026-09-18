# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while True:
            node = prev

            for _ in range(k):
                node = node.next
                if not node:
                    return dummy.next

            group_end = node
            curr = prev.next
            next_group = group_end.next
            prev_group = next_group

            while curr != next_group:
                temp = curr.next
                curr.next = prev_group
                prev_group = curr
                curr = temp

            temp = prev.next
            prev.next = group_end
            prev = temp
