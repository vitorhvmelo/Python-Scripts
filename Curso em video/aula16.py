#cont = ('um', 'dois', 'tres', 'quatro','cinco',
#        'seis', 'sete', 'oito', 'nove', 'dez'  )
#
#num = int(input('Digite um numero de 1 a 10: '))
#
#print(cont[num-1])



#from random import randint
#tupla = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
#maior=0
#menor=10
#for c in tupla:
#    if c > maior:
#        maior = c
#    if c < menor:
#        menor = c
#print(f'Os numeros sao {tupla}')        
#print(f'O menor numero é {menor}, e o maior é {maior}')
##Jeito melhor de fazer
#print(f'O menor numero é {min(tupla)}, e o maior é {max(tupla)}')


palavra = ('zuleica', 'Jacinto', 'leite', 'aquino', 'rego')

for p in palavra:
    print(f'A palavra {p.upper()} tem as vogais: ', end='')
    for letra in p: #P é tbm uma lista de letras
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
    print('\n')