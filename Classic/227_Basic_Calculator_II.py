'''
Implement a basic calculator to evaluate a simple expression string
1. if operator is + or -, put number into stack.
2. if operator is x or /, pop number from stack and do x or / with current number.
3. if encounter last index, we should do step1 & step2.

Example: 
"3+2*2" = 7
"10-4+2*3+4/2 = 14
'''


def calculate(self, s: str) -> int:
    stack = []
    current_num = 0
    operator = '+'
    
    numbers = [str(x) for x in range(10)]
    all_operators = ['+', '-', '*', '/']
    if not s :
        return 0
    
    for indx in range(len(s)):
        char = s[indx]
        
        if char in numbers:
            current_num = current_num * 10 + int(char)
            
        if char in all_operators or indx == len(s) - 1:
            if operator == '+':
                stack.append(current_num)
            elif operator == '-':
                stack.append(-current_num)
            elif operator == '*':
                stack[-1] = stack[-1] * current_num
            elif operator == '/':
                stack[-1] = int(stack[-1] / current_num)
            
            current_num = 0
            operator = char
    return sum(stack)