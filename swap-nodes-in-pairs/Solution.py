# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if (not head or not head.next):
            return head
        else:
            first_node = head
            second_node = head.next

            # Swapping
            first_node.next  = self.swapPairs(second_node.next)
            second_node.next = first_node

            # Now the head is the second node
            return second_node
