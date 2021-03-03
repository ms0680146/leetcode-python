'''
Stack
用於記住之前的狀態。
1. Init Stack
2. for loop asteroids
3. if asteroid > 0 --> push to stack
4. else --> keep pop smaller asteroid until stack is empty or top element < 0

Edge Case: 相等的情形 or stack peek < 0
'''
def asteroidCollision(asteroids):
    stack = []
    for i in range(len(asteroids)):
        if asteroids[i] > 0:
            stack.append(asteroids[i])
        else:
            while len(stack) > 0 and stack[-1] > 0 and stack[-1] < -asteroids[i]:
                stack.pop(-1)
            
            if len(stack) > 0 and stack[-1] == -asteroids[i]:
                stack.pop(-1)
            elif len(stack) == 0 or stack[-1] < 0:
                stack.append(asteroids[i])
                
    return stack