# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:       # if both ListNodes are empty
            return ListNode(0)
        old = ListNode(0)   
        cur = old
        add_in = 0
        while l1 or l2 or add_in:
            t1 = 0 if not l1 else l1.val
            t2 = 0 if not l2 else l2.val
            add_in, out = divmod(t1 + t2 + add_in, 10)
            cur.next = ListNode(out)
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return old.next
            
        
