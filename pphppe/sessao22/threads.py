"""
GIL - Python Global Interpreter Lock, ou simplesmente  GIL, é um mutex (ou lock) q permite q apenas
uma thread tome conta do interpretador Python.


from threading import Thread

cont = 50000000

def contagem_regressiva(n):
    while n > 0:
        n -= 1

# Single-thread
inicio = time.time()
contagem_regressiva(cont)
final = time.time()

print(f'Tempo em segundos: {final - inicio}') # 7.997093200683594

# Multi-thread
t1 = Thread(target=contagem_regressiva, args=(cont//2,)) # Colocandoo a execução da função na Thread t1.
t2 = Thread(target=contagem_regressiva, args=(cont//2,))

inicio = time.time()
t1.start() # Startar thread.
t2.start()
t1.join() # Executar thread.
t2.join()
final = time.time()

print(f'Tempo em segundos: {final - inicio}') # 8.362904787063599

# Como pode ser visto, mesmo utilizando múlti-thread o tempo de finalização n muda muito.

# A Utilização da GIL prejudica a real utlilização de multi-cores nas máquinas, o que tornas os
# projetos Python lentos em alguns casos.

# Por outro lado, o GIL torna as aplicações single-thread muito performáticas, assim a grande maioria das
# aplicações n precisam utilizar multi-threads.

"""

import time

# Caso vc tenha problemas com o GIL, vc pode utilizar o multi-processing ao invés do multithreading.
# Utilizando processos ao invés de threads, cada processo Python ganha seu próprio interpretador Python
# e espaço em memória. Dessa forma o GIL n será problema.

from multiprocessing import Pool

cont = 50000000

def contagem_regressiva(n):
    while n > 0:
        n -= 1

if __name__ == '__main__':
    pool = Pool(processes=2)
    inicio = time.time()
    r1 = pool.apply_async(contagem_regressiva, [cont//2])
    r2 = pool.apply_async(contagem_regressiva, [cont//2])
    pool.close()
    pool.join()
    final = time.time()

    print(f'Tempo em segundos: {final - inicio}') # 3.179328203201294 (no entanto ele foi executado sozinho com os códigos acima como comentário).

# OBS: Multi-processing são mais pesados do q multi-threading.
# Ou seja, para cada processo, teremos um ambiente Python próprio.