"""
import random

# Versão 1 - Sem annotations

NAIPES = '♠ ♡ ♢ ♣'.split()

TIPOS = '2 3 4 5 6 7 8 9 10 11 J Q K A'.split()

def criar_baralho(embaralhar=False):
    baralho = [(tipo, naipe) for tipo in TIPOS for naipe in NAIPES]

    if embaralhar:
        random.shuffle(baralho)
        return baralho
    return baralho

def distribuir_cartas(baralho):
    '''Gerencia a mão de acordo com o baralho gerado'''
    # É como se desse uma carta por vez a cada jogador (o primeiro jogador só receberá a 2 carta depois de um intervalo de 4).
    return (baralho[0::4], baralho[1::4], baralho[2::4], baralho[3::4])

def jogar():
    '''Inicia um jogo de cartas para 4 jogarores'''
    cartas = criar_baralho(embaralhar=True)
    jogadores = 'J1 J2 J3 J4'.split()
    maos = {j: m for j, m in zip(jogadores, distribuir_cartas(cartas))}

    for jogar, cartas in maos.items():
        carta = ' '.join(f'{tipo}{naipe}' for (tipo, naipe) in cartas)
        print(f'{jogar}: {carta}')

if __name__ == '__main__':
    jogar()

"""

import random
from typing import List, Tuple, Dict

# Versão 2 - Com annotations

NAIPES: List[str] = '♠ ♡ ♢ ♣'.split()

TIPOS: List[str] = '2 3 4 5 6 7 8 9 10 11 J Q K A'.split()

CARTA = Tuple[str, str]
BARALHO = List[CARTA]

def criar_baralho(embaralhar: bool=False) -> BARALHO:
    baralho: BARALHO = [(tipo, naipe) for tipo in TIPOS for naipe in NAIPES]

    if embaralhar:
        random.shuffle(baralho)
        return baralho
    return baralho

def distribuir_cartas(baralho: BARALHO) -> Tuple[BARALHO, BARALHO, BARALHO, BARALHO]:
    """Gerencia a mão de acordo com o baralho gerado"""
    # É como se desse uma carta por vez a cada jogador (o primeiro jogador só receberá a 2 carta depois de um intervalo de 4).
    return (baralho[0::4], baralho[1::4], baralho[2::4], baralho[3::4])

def jogar() -> None:
    """Inicia um jogo de cartas para 4 jogarores"""
    cartas: BARALHO = criar_baralho(embaralhar=True)
    jogadores: List[str] = 'J1 J2 J3 J4'.split()
    maos: Dict[str, BARALHO] = {j: m for j, m in zip(jogadores, distribuir_cartas(cartas))}

    for jogar, cartas in maos.items():
        carta: str = ' '.join(f'{tipo}{naipe}' for (tipo, naipe) in cartas)
        print(f'{jogar}: {carta}')

if __name__ == '__main__':
    jogar()