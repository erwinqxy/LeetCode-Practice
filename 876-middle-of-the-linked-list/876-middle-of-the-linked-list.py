# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
      p1 = head     # 2 step pointer
      p2 = head     # 1 step pointer 
      
      while (p1 and p1.next):
        p1 = p1.next.next 
        p2 = p2.next
      return p2
      

# Approach
# Two points, one with one step and other with two step
# when the one with two step reached the end of the linked list, the 
# one step pointer would be in the middle 

# Time = O(log n)  -> halving the search time by half with two step pointer
# Space = O(1)