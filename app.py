menor_valor = None
maior_valor = None
for i in range(5):
    valor = int(input("Digite um valor inteiro: "))
    if menor_valor is None or valor < menor_valor:
        menor_valor = valor
    else:
        maior_valor = valor

print('O maior valor é', maior_valor, 'e o menor valor é', menor_valor)
