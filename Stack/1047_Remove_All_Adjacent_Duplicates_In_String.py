'''
Stack

Input: "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, 
and this is the only possible move.  
The result of this move is that the string is "aaca", 
of which only "aa" is possible, so the final string is "ca".

使用一個 Stack
從字串的左邊開始掃描
Stack 的 Top 會紀錄目前最新的字元
如果下 1 個字元和 Top 一樣
則 Top 要移除掉
否則都一直加進 Stack。
'''

def removeDuplicates(S):
    stack = []
    for char in S:
        if len(stack) == 0:
            stack.append(char)
        elif stack[-1] != char:
            stack.append(char)
        else:
            stack.pop(-1)
    ans = ''
    for char in stack:
        ans += char
    return ans
