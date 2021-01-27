'''
Solution: Linked List & Two Pointers

dummy
-1    ->    1    ->    2    ->    3    ->    4    ->    5    ->    None
fast
slow
-------
讓 fast 先走 2 單位
-1    ->    1    ->    2    ->    3    ->    4    ->    5    ->    None
slow -------2------- fast
-------
直到fast.next = None 時, slow都維持兩單位的差
-1    ->    1    ->    2    ->    3    ->    4    ->    5    ->    None
                                 slow -------2------- fast
-------
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
    dummy = ListNode(-1)
    dummy.next = head

    fast = dummy
    slow = dummy

    # 讓 fast 先走 n 單位
    for _ in range(n):
        fast = fast.next
    
    while fast.next != None:
        fast = fast.next
        slow = slow.next
    
    slow.next = slow.next.next
    return dummy.next

print(removeNthFromEnd([1,2,3,4,5], 2)) # [1,2,3,5]