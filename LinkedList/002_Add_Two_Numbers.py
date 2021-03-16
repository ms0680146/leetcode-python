'''
有用到 carry 來紀錄進位。

General case:
l1 = [2,4,3], l2 = [5,6,4] -> result = [7,0,8]

Edge case(l1 or l2 = None):
l1 = None, l2 = [5,6,4] -> result = [5,6,4]

Edge case(l1 > l2 or l2 > l1):
l1 = [2,4,3,6], l2 = [5,6,4] -> result = [7,0,8,6]

Edge case:
l1 = [2,4,6], l2 = [5,6,4] -> result = [7,0,1,1]
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    if l1 == None:
        return l2

    if l2 == None:
        return l1
        
    # create dummy
    dummy = ListNode(-1)
    result = dummy
    carry = 0 

    # loop l1, l2
    while l1 != None and l2 != None:
        result.next = ListNode((l1.val + l2.val + carry) % 10)
        carry = (l1.val + l2.val + carry) // 10
        l1 = l1.next
        l2 = l2.next
        result = result.next

    # remaining l1
    while l1 != None:
        result.next = ListNode((l1.val + carry) % 10)
        carry = (l1.val + carry) // 10
        l1 = l1.next
        result = result.next

    # remaining l2
    while l2 != None:
        result.next = ListNode((l2.val + carry) % 10)
        carry = (l2.val + carry) // 10
        l2 = l2.next
        result = result.next

    if carry == 1:
        result.next = ListNode(1)

    return dummy.next

print(addTwoNumbers([2,4,3], [5,6,4])) # [7,0,8]

