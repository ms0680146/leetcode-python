'''
FizzBuzz
給定一個數字 n，依照以下規則列出所有的數字。
3 的倍數要呈現 Fizz
5 的倍數要呈現 Buzz
15 的倍數要呈現 FizzBuzz
'''

def fizzBuzz(n):
    result = []
    for i in range(1, n+1): # 1,2,...16
        if i % 15 == 0:
            result.append('FizzBuzz')
        elif i % 3 == 0:
            result.append('Fizz')
        elif i % 5 == 0:
            result.append('Buzz')
        else:
            result.append(str(i))
    return result      