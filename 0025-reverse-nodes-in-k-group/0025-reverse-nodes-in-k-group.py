# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        d = ListNode(0)
        d.next = head
        p = d

        while True:
            q = p
            for _ in range(k):
                q = q.next
                if not q:
                    return d.next

            a = p.next
            b = a.next

            for _ in range(k - 1):
                a.next = b.next
                b.next = p.next
                p.next = b
                b = a.next

            p = a