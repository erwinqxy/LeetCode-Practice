# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        data = {}
        i = 0
        if (head is None):
          return None 
        while (head.next != None ):
          if (head in data):
            return head
          else:
            data[head] = i 
            i+= 1
            head = head.next
        return None