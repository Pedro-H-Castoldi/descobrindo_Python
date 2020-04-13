import pagamento
from compra import Compra
import salvar_cliente

class Cliente:

    l_clientes = []

    def __init__(self, nome, idade, cpf, endereco):
        self.__id = Cliente.l_clientes[len(Cliente.l_clientes) - 1].id + 1
        self.__nome = nome.title().strip()
        self.__idade = idade
        self.__cpf = cpf.strip()
        self.__endereco = endereco.title().strip()
        self.__estado = False

    @property
    def id(self):
        return self.__id
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome_e):
        self.__nome = nome_e
    @property
    def idade(self):
        return self.__idade
    @idade.setter
    def idade(self, idade_e):
        self.__idade = idade_e
    @property
    def cpf(self):
        return self.__cpf
    @cpf.setter
    def cpf(self, cpf_e):
        self.__cpf = cpf_e
    @property
    def endereco(self):
        return self.__endereco
    @endereco.setter
    def endereco(self, endereco_e):
        self.__endereco = endereco_e
    @property
    def estado(self):
        return self.__estado
    @estado.setter
    def estado(self, novo):
        self.__estado = bool(novo)

    def add(self):
        Cliente.l_clientes.append(self)

    @classmethod
    def mudar_estatus(cls, cli):
        for cliente in Cliente.l_clientes:
            if cli.id == cliente.id:
                if cliente.estado:
                    cliente.estado = False
                else:
                    cliente.estado = True
    @classmethod
    def listar_clientes(cls):
        for cliente in Cliente.l_clientes:
            print(f'ID Cliente: {cliente.id} - Nome: {cliente.nome} - Idade: {cliente.idade} - CPF: {cliente.cpf} - Endereço: {cliente.endereco} - Status: {cliente.estado}')

    @classmethod
    def listar_clientes_nome(cls, nome):
        encontrado = False
        cont_ex = 0
        for cliente in Cliente.l_clientes:
            cont_ex += 1
            if(cliente.nome == nome):
                encontrado = True
                print(f'ID Cliente: {cliente.id} - Nome: {cliente.nome} - Idade: {cliente.idade} - CPF: {cliente.cpf} - Endereço: {cliente.endereco} - Status: {cliente.estado}')
                op = int(input('1- Histórico de Pagamentos | 2- Histórico de Compras | 3- Editar | 4- Excluir | 0- Voltar: '))
                if op == 1:
                    pagamento.Pagamento.historico_de_pagamento(cliente.id)
                    break
                elif op == 2:
                    Compra.historico_de_compras_cliente(cliente.id)
                    break
                elif op == 3:
                    while True:
                        op2 = int(input('1- Nome | 2- Idade | 3- CPF | 4- Endereço | 0- Cancelar: '))
                        if op2 == 1:
                            nome_e = str(input(f'Nome- {cliente.nome}: ')).title()
                            cliente.nome = nome_e
                            salvar_cliente.salvar_cliente()
                            print('Cliente editado com sucesso.')
                        elif op2 == 2:
                            idade_e = int(input(f'Idade- {cliente.idade}: '))
                            cliente.idade = idade_e
                            salvar_cliente.salvar_cliente()
                            print('Cliente editado com sucesso.')
                        elif op2 == 3:
                            cpf_e = str(input(f'CPF- {cliente.cpf}: '))
                            cliente.cpf = cpf_e
                            salvar_cliente.salvar_cliente()
                            print('Cliente editado com sucesso.')
                        elif op2 == 4:
                            endereco_e = str(input(f'Endereço- {cliente.endereco}: ')).title()
                            cliente.endereco = endereco_e
                            salvar_cliente.salvar_cliente()
                            print('Cliente editado com sucesso.')
                        else:
                            break
                elif op == 4:
                    op2 = int(input(f'1- Confirmar exclusão do cliente: {cliente.nome} | 2- Cancelar: '))
                    if op2 == 1:
                        print(f'O cliente: {cliente.nome} foi excluído com sucesso.')
                        Cliente.l_clientes.pop(cont_ex - 1)
                        salvar_cliente.salvar_cliente()
                else:
                    break
        if not encontrado:
            print('Cliente não encontrado.')
    @classmethod
    def cliente_dados(cls, nome):
        for cliente in Cliente.l_clientes:
            if (cliente.nome == nome):
                return cliente

        print('Cliente não encontrado.')