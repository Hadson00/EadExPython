def contaDigito(n):
    return len( str(n) )
def exibe():
    n = int(input('Digite um número: '))
    print(contaDigito(n),'dígitos')
    
while True:
    exibe()