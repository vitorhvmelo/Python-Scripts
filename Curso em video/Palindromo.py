word = input('Digite uma palavra para testar ou exit para sair: ').lower().strip()

while (word != 'exit'):
    index = len(word) -1
    contrario = word
    numero = 0
    for c in range(0, index+1, 1):
        if contrario[c] == word[index - c]:
            numero += 1

    if numero == len(word):
        print('A palavra é um palindromo')
    else:
        print('A palavra digitada nao é um palindromo')

    word = input('Digite uma palavra para testar ou exit para sair ').lower().strip()