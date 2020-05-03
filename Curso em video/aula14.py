# #exercicio 57: ler sexo
#
# sexo = str(input('Sexo')).upper().strip()[0] #so quero a primeira letra
# while sexo not in 'MF':
#     sexo = str(input('Sexo: ')).upper().strip()[0]
# print('fim')


#exercicio 58: adivinha numero
#
# from random import randint
# computador = randint(1,10)
# num = int(input('Digite um numero: '))
# while num != computador:
#     print('Eroooou')
#     num = int(input('Digite um numero: '))

#exercicio 62: Super PA
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razao: '))
print(primeiro, end=' → ')
soma = primeiro
c = 2
while c <= 10:
     soma += razao
     print(soma, end=' → ')
     c+=1
print('Acabou')
mais = int(input('Mais quantos numeros: '))
d=1
while d <= mais:
     soma += razao
     print(soma, end=' → ')
     if d == mais:
         print("Fim")
     d+=1
     if mais == 0:
         d = mais
         print("Digitou 0")

