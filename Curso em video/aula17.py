##exercicio 78: Inserir valores na lista e maior e menor
#
#lista = []
#for c in range(0,5):
#    lista.append(int(input(f'Digite um valor para a posiçao {c}: ')))
#
#print(f'O maior valor é {max(lista)} e o menor é {min(lista)}')


#exercicio 79

lista = list()
while True:
    n = str(input('Deseja adicionar um item [S/N]: ')).upper().strip()[0]
    if n != 'S':
        break
    z = int(input('Digite um valor: '))
    if z not in lista:
        lista.append(z)
    else:
        print('\a Valor duplicado!')
lista.sort()
print(f'A lista em ordem é {lista}')
    
    