# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        pq=[]
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(pq, (head.val, i, head))
        dummy = cur = ListNode()
        while pq:
            val, i, node = heapq.heappop(pq)
            if node.next:
                heapq.heappush(pq, (node.next.val, i, node.next))
            cur.next = node
            cur = cur.next
        return dummy.next