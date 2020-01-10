# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode: # use recursion
        merged = ListNode(0)
        cur = merged
        while l1 or l2:
            if not l1:  # ListNode l1 is empty
                cur.next = l2   # shallow copy
                break
            if not l2:
                cur.next = l1
                break
            else:
                cur.next = ListNode(0)
                cur = cur.next
                if l1.val <= l2.val:
                    cur.val = l1.val
                    l1 = l1.next
                else:
                    cur.val = l2.val
                    l2 = l2.next
                
        return merged.next
                
        
