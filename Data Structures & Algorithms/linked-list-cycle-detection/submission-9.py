# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hm = set() 
        curr = head
        while curr:
            if curr in hm:
                return True 
            hm.add(curr)
            curr = curr.next 
        return False