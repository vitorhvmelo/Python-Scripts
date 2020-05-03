# #exercicio 47

# for c in range(0, 51, 2):
#     print(c, end='  ')



#exercicio 48 soma dos numeros impares  divisiveis por 3 de 1 ate 500

# soma = 0
# num = 0
# for c in range(3, 501, 3):
#     if c % 2 != 0:
#         print(c, end='  ')
#         soma += c
#         num += 1
#
# print('\n A soma dos {} numeros é {}'.format(num, soma))

# #exercicio 49 Tabuada com FOR
#
# num = int(input('Digite um numero para ver sua tabuada: '))
# for c in range(0, 11, 1):
#     print('{} x {:2} = {}'.format(num, c, num*c))

# #exercicio 50 Ler 6 numeros e mostrar a soma dos pares
#
# soma = 0
# for c in range(0, 6):
#     num = int(input('Digite um numero: '))
#     if num%2 == 0:
#         soma += num
# print(soma)

#exercicio 51: 10 primeiros termos de uma PA

# primeiro = int(input('Primeiro termo: '))
# razao = int(input('Razao: '))
# print(primeiro, end=' → ')
# soma = primeiro
# for c in range(1, 10):
#     soma += razao
#     print(soma, end=' → ')
# print('Acabou')

#exercicio 56: Ler nome, idade e sexo e mostrar media de idade nome do homem mais velho e numero de mulheres menos de 20 anos
idade = 0
maior = 0
media = 0
k = 0
for c in range(1, 5):
    print('----- {}º PESSOA -----'.format(c))
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip().upper()
    if idade > maior and sexo == 'M':
        maior = idade
        nomeVelho = nome

    if idade < 20 and sexo == 'F':
        k += 1
        print(k)

    media += idade
print('''\n\n Media de idades: {}
Nome do M mais velho: {}
Nº de mulheres < 20: {}'''.format(media/5, nomeVelho, k))
