"""
Max este o pisica mare care doarme toata ziua.
obiect -> Max
clasa -> Pisica
proprietate -> mare
activitate -> doarme

LIFO -> Last in First Out
FIFO -> First in First out
"""

stiva = []


def push(val):
    stiva.append(val)


def pop():
    val = stiva[-1]
    del stiva[-1]
    return val


push(3)
push(2)
push(1)
print(pop())
print(pop())
print(pop())