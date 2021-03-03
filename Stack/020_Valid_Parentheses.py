'''
Solution: Stack & Map

if counter (, [, { -> store into stack.
if counter ), ], } -> pop from stack, check is pair or not.
'''
def isValid(s):
    stack = []
    mapping = {')': '(', ']':'[', '}':'{'}

    for parentheses in s:
        if parentheses in ['(', '[', '{' ]:
            stack.append(parentheses)
        else: # three case: ), ], }
            if len(stack) == 0:
                return False
            
            if stack.pop() != mapping[parentheses]:
                return False

    return len(stack) == 0

print(isValid("()")) # true
print(isValid("()[]{}")) # true
print(isValid("(]")) # false
print(isValid("]")) # false