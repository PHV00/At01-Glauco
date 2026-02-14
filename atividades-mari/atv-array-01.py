""" 
Atividade: Adicionando um ao número representado como matriz de dígitos

Dado um número não negativo representado como uma matriz de dígitos.
A tarefa é somar 1 ao número (aumentar por 1 o número representado pelos algarismos). 
Os dígitos são armazenados de forma que o dígito mais significativo seja o primeiro elemento da matriz.

Ex: 
Entrada : [9, 9, 9]
Saída: 1000
Explicação: 999 + 1 = 1000

Fonte: https://www.geeksforgeeks.org/dsa/adding-one-to-number-represented-as-array-of-digits/
"""

# V1 - Feita por mim
# numArr = [1, 2, 3]
# numStr = ""

# for n in numArr:
#     numStr += str(n)

# num = int(numStr)

# print(f"Número do array: {num}")

# num = num + 1

# print(f"Número do array + 1: {num}")

# V2 - Refatorado pela IA e explicado linha a linha com comentários
numArr = [1, 2, 3]

n = len(numArr)

# Percorre o array de trás para frente (último dígito até o primeiro)
for i in range(n - 1, -1, -1):

    # Se o dígito atual for menor que 9,
    # podemos simplesmente somar 1 e encerrar o processo
    if numArr[i] < 9:
        numArr[i] += 1
        break   # sai do loop porque o incremento já foi feito corretamente

    # Se o dígito for 9, ele vira 0 (vai "um" para a casa da esquerda)
    else:
        numArr[i] = 0

# Esse else do for só executa se o loop terminar SEM break
# Ou seja: todos os dígitos eram 9 (ex: [9,9,9])
else:
    # Insere 1 no início do array → ex: [9,9,9] vira [1,0,0,0]
    numArr.insert(0, 1)

# Converte o array de dígitos para número inteiro:
# [1,2,4] → "124" → 124
resultado = int("".join(map(str, numArr)))

print("Saída:", resultado)