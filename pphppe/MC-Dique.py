"""
Deque -> É uma lista de alta performance
"""

from collections import deque
deq = deque('Pedro')
print(deq)

deq.append(' ')
print(deq)
deq.appendleft('P') # Com o Deque é possivel adicionar elementos no inicio da lista (antes só dava no final)
print(deq)

# Remover o primeiro elemento
print(deq.popleft())
print(deq)