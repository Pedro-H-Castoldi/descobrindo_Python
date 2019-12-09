"""
Dunder Name e Dunder Main (main significa principal)

Dunder -> Double Under ('__');

    Dunder Name -> __name__ ;

    Dunder Main -> __main__ .

Em Python, são utilizadas a dunders para criação de funções, atributis, propriedades, etc
isso para n gerar conflito com os nomes desses elementos na programação.

# Em outras linguagens, é necessário criar a classe main para se dar início o programa, por exemplo:
    Linguagem C
    int main(){
        return 0;
        }

Já em Python, se for executado um módulo Python diretamente na linguagem de comando, internamente
o Python atribuirá à variável __name__ o valor __main__ indicando q esse módulo é o
módulo de execução principal.


Para tirar os prints das importações de módulos, se utiliza a seguinte condição:
if __name__ == '__main__':
    numeros = [1, 6, 3]
    print(numeros)

Desta forma o print só será executado caso esse arquivo esteja sendo executado como principal (main), senão estiver,
somente a variável 'numeros' será importada.

"""

# EX
from funções_com_parâmetro import nome_completo
print(nome_completo('Pedro', 'Castoldi'))

