def question1(inputList):
    def func(x):
        return x + x[-1] * (maxLen - len(x))

    maxLen = 0
    
    inputStr = [str(num) for num in inputList]
    for num in inputStr:
        n = len(str(num))
        if maxLen<n:
            maxLen = n
    inputStr.sort(key=func, reverse=True)
    print("".join(inputStr))
    
if __name__ == '__main__':
    a = [3,30,9,5]
    question1(a)
