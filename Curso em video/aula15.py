
#=============================================================================
#exercicio 66
# n = c = soma = 0
# while True:
#     n = int(input('Digite um valor [999 para parar]:  '))
#     if n == 999:
#         break
#     c += 1
#     soma += n
# 
# print(f'A soma dos {c} numeros é {soma} ')
#=============================================================================

# =============================================================================
#exercicio 68 Jogo par ou impar

from random import randint

while True:
    pc = randint(1,100)
    num = int(input('Digite um valor [0 para sair]: '))
    if num == 0:
        break
    pi = str(input('Par ou Impar: ')).strip().upper()[0]
    
    if pi == 'P':
        if (num+pc) % 2 == 0:
            print('Vc ganhou')
        else:
            print('Vc perdeu')
    if pi == 'I':
        if (num+pc) % 2 != 0:
            print('Vc ganhou')
        else:
            print('Vc perdeu')
# =============================================================================
