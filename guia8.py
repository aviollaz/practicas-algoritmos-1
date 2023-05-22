#3--------------
import math
def suma_total(x:list) -> int:
    n: int = 0

    for i in range(0, len(x)):
        n = n + x[i]
    
    return n

print(suma_total([1,2,3,4,5]),"\n")

def ordenados(x:list) -> bool:
    res = True
    for i in range(0, len(x)-1):
        if x[i] >= x[i+1]:
            res = False
            break
    return res

print(ordenados([1,2,3,4,5]), "\n")

def palindroma(x:list) -> bool:
    res = True
    for i in range(0, math.floor(len(x)/2)):
        if x[i] != x[len(x)-i-1]:
            res = False
            break
    return res

x = "asddwsa"
print(palindroma(x))
