x = int(input("Digite um número: "))
ant = 0
prox = 1
soma = 1


if x < 100:
    for i in range(x,101):
        print(ant)
        soma = prox + ant
        ant = prox
        prox = soma