'''
Solution: Array, Pointer

從list最後面往前看
如果數字小於9，加上1後返回該list.
如果遇到9，則將此數字改為0，跑下一次迴圈.
[1,2,9] -> [1,3,0]
[1,9,9] -> [2,0,0]
[9,9,9] -> [1,0,0,0]
'''
def plusOne(digits):
    idx = len(digits)-1 # 3-1=2
    while idx >= 0:
        if digits[idx] < 9:
            digits[idx] += 1
            return digits
        else:
            digits[idx] = 0
        idx -= 1
    # case: [9,9,9] -> [1,0,0,0]
    digits.insert(0,1)
    return digits

    
print(plusOne([1,2,3])) # [1,2,4]
print(plusOne([4,3,2,1])) # [4,3,2,2]
print(plusOne([0])) # [1]

