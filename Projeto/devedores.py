from variaveis_g import *

def devedores():
    print('ID Compra         ID Cliente         Nome            Produto(s)')
    for i in devendo:
        print(f'{i}          {devendo[i][0]}    {devendo[i][1][0]}            {devendo[i][2]}')