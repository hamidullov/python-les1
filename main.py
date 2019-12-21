# -*- coding: utf-8 -*-
n = 0
def inputInt(s):
    result = 0
    while result == 0:
        resultStr = input(s + ": ") 
        if resultStr.isdigit():
            result=int(resultStr)
        else: 
            print(f"{resultStr} не является числом")
    return result


MAX_ATTEMPTS = 30

n = inputInt("введите количество попыток")
while n > MAX_ATTEMPTS:
    n = inputInt("введите количество попыток")

s = []
for i in range(1,n+1):
    m = inputInt("введите число")
    if m%4 != 0:
        s.append(m)

print(s)
print("количество:", len(s))

print("пока")