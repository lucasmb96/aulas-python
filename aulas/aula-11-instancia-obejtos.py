#import stdiomask

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
        self.titular = titular
        self.saldo = saldo
        self.pin = pin
        self.limite = 400
    

    def levantamento(self, valor):
        confirma_pin = input('Digite o pin: ', '*')
        
        if confirma_pin == self.pi:
            if valor <= self.limite:
                self.saldo -= valor
            else:
                print(f'Ultrapassou o limite {self.limite:.2f}$')
        else:
            print('Pin invalido')



nova_conta = Conta('Ricardo', 5000, '1234')

print(nova_conta.saldo)

nova_conta.levantamento 
