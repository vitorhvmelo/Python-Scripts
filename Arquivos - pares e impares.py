pares = open('pares.txt', 'w')
impares = open('impares.txt', 'w')

for t in range(0, 1000):
    if t % 2 == 0:
        pares.write(f"{t}\n")
    else:
        impares.write(f"{t}\n")

pares.close()
impares.close()