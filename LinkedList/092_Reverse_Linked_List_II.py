'''

Example:
https://www.youtube.com/watch?v=wk8-_M-2fzI&ab_channel=leetuition
Need 3 pointer: pre, cur, Next
Need dummy present as first node
1 -> 2 -> 30 -> 40 -> 50 -> 60 -> null, m=3/n=6

1 -> 2 -> 40 -> 30 -> 50 -> 60 -> null

1 -> 2 -> 50 -> 40 -> 30 -> 60 -> null

1 -> 2 -> 60 -> 50 -> 40 -> 30 -> null
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseBetween(head, m, n):
    # create dummy
    dummy = ListNode(-1)
    dummy.next = head

    # create pre
    pre = dummy
    for _ in range(m-1): # 0,1
        pre = pre.next
    
    cur = pre.next
    while m < n:
        Next = cur.next
        cur.next = Next.next
        Next.next = pre.next
        pre.next = Next
        m += 1

    return dummy.next
    


print(reverseBetween([1,2,3,4,5], 2, 4)) #1->4->3->2->5->NULL

