import stdiomask

def deposito(conta, valor):
    global saldo
    global pin

    confima_pin == pin

    if confirma_pin == pin:
        saldo += valor
    else:
        print('Pin invalido')

class Conta:
    def __init__(self, titular, saldo, pin):
        self.__titular = titular
        self.__saldo = saldo
        self.__pin = pin
        self.__limite = 400
    

    def get_saldo(self):
        confirma_pin = input('Digite pin: ')

    
    def set_pin(self):
        confirma_pin = input('Digite pin antigo: ')
        if confima_pin == self.pin:
            


    def levantamento(self, valor):
        confirma_pin = stdiomask.getpass(input('Digite o pin: ', '*'))
        
        if confirma_pin == self.pi:
            if valor <= self.limite:
                self.saldo -= valor
            else:
                print(f'Ultrapassou o limite {self.limite:.2f}$')
        else:
            print('Pin invalido')



nova_conta = Conta('Ricardo', 5000, '1234')
