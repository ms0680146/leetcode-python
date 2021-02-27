'''
用 Recursion 的方式來解
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def reverseList(head):
    # Base Case
    if head is None or head.next is None:
        return head
    # 向子問題要答案
    reversed_head = reverseList(head.next)
    # 利用子問題的答案建構當前問題的答案
    head.next.next = head
    head.next = None
    # 返回值給父問題
    return reversed_head