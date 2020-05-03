  #DESAFIO 36
 preco = float(input("Qual o valor da casa?"))
 salario = float(input("Qual o seu salario?"))
 anos = int(input("Em quantos vai pagar?"))
 meses = anos * 12
 minimo = 0.3 * salario
 parcela = preco/meses

 print ('Para pagar uma casa de R${:.2f} em {} anos a presataçao sera R${:.2f}'.format(preco, anos, parcela), end='   ') #end mostra o que fazer no final da linha, o padrao é um enter,
                                                                                                                         #se colocar vazio, o proximo print fica na frente
 print('Valor da parcela')
 if parcela <= minimo:
     print("Emprestimo aprovado")
 else:
     print("Emprestimo negado")

# # DESAFIO 37
num = int(input('Digite um numero inteiro: '))
print('''Escolha uma base de conversao:
 [ 1 ] BINARIO
 [ 2 ] OCTAL
 [ 3 ] HEXADECIMAL ''') # 3 ASPAS CONSIDERA OS ENTERS, PORTANTO O PRINT RESPEITARA A QUEBRA DE LINHA QUE FIZEMOS
opcao = int(input('Sua opçao: '))
if opcao == 1:
    print('{} convertido para Bin fica {}'.format(num, bin(num)[2:])) # O 2: faz com que so mostre do terceiro digito ate o final
elif opcao == 2:
    print('{} convertido para Octal fica {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para Hex fica {}'.format(num, hex(num)[2:]))
else:
    print('opçao invalida')