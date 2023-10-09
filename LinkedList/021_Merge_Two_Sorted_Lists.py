'''
Solution: Linked List
1. create dummy node.
2. create empty linked list.
3. compare two linked lists.
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1, l2):
    # Edge Case:
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    
    # create dummy
    dummy = ListNode()
    # create new linked list
    new = dummy

    # While loop compare two linked list.
    while l1 and l2:
        if l1.val > l2.val:
            new.next = ListNode(l2.val)
            l2 = l2.next
        else:
            new.next = ListNode(l1.val)
            l1 = l1.next
        new = new.next
    
    if l1:
        new.next = l1

    if l2:
        new.next = l2
    
    return dummy.next


print(mergeTwoLists([1,2,4], [1,3,4])) # [1,1,2,3,4,4]