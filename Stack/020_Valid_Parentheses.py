'''
Solution: Stack & Map

if counter (, [, { -> store into stack.
if counter ), ], } -> pop from stack, check is pair or not.
'''
def isValid(s):
    stack = []
    mapping = {')':'(', '}':'{', ']':'['}
    
    for parentheses in s:
        if parentheses in ['(', '{', '[']:
            stack.append(parentheses)
        elif len(stack) == 0:
            return False
        elif stack.pop() != mapping[parentheses]:
            return False
    return stack == []

print(isValid("()")) # true
print(isValid("()[]{}")) # true
print(isValid("(]")) # false
print(isValid("]")) # false