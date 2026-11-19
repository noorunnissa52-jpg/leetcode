# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        arr = []
        while list1:
            arr.append(list1.val)
            list1 = list1.next
        while list2:
            arr.append(list2.val)
            list2 = list2.next
        
        # 2. Bubble Sort on arr
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        
        # 3. Convert arr back to Linked List
        dummy = ListNode(0)
        curr = dummy
        for val in arr:
            curr.next = ListNode(val)
            curr = curr.next
        
        return dummy.next