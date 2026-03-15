""" 
-------------------------------------------------------------------------------------------------------------------------------------
Disciplina: Algoritmos Avançados   
Curso: Engenharia de Software  
Aluno(a): Marina Rosa Oliveira
Professor: Glauco Scheffel
-------------------------------------------------------------------------------------------------------------------------------------

Problema: Adding one to number represented as array of digits

-> Complexidade:
Tempo: O(n)
Memória: O(1)

-> Estrutura principal utilizada: Array - Nível fácil

-> Descrição do problema:
Dado um número não negativo representado como uma matriz de dígitos.
A tarefa é somar 1 ao número (aumentar por 1 o número representado pelos algarismos). 
Os dígitos são armazenados de forma que o dígito mais significativo seja o primeiro elemento da matriz.

-> Utilização da IA
Neste exercício, a IA foi utilizada para refatorar o código e explicar sua refatoração linha a linha, de forma a facilitar a compreensão da nova lógica. Além disso,
foi utilizada para melhorar a clareza da documentação.

Fonte: https://www.geeksforgeeks.org/dsa/adding-one-to-number-represented-as-array-of-digits/
"""

import unittest

# V1 - Feita por mim
def solucao_v1(numArr):
    numStr = ""

    for n in numArr:
        numStr += str(n)

    num = int(numStr)

    num = num + 1

    return num


# V2 - Refatorado pela IA e explicado linha a linha com comentários
def solucao_v2(numArr):

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

    return resultado

# =========================
# TESTES UNITÁRIOS
# =========================
class TestPlusOne(unittest.TestCase):

    # Teste 1: todos os dígitos são 9
    # 999 + 1 = 1000
    def test_todos_nove(self):
        arr = [9, 9, 9]

        self.assertEqual(solucao_v1(arr.copy()), 1000)
        self.assertEqual(solucao_v2(arr.copy()), 1000)


    # Teste 2: incremento simples sem carry
    # 124 + 1 = 125
    def test_incremento_simples(self):
        arr = [1, 2, 4]

        self.assertEqual(solucao_v1(arr.copy()), 125)
        self.assertEqual(solucao_v2(arr.copy()), 125)


    # Teste 3: número zero
    # 0 + 1 = 1
    def test_zero(self):
        arr = [0]

        self.assertEqual(solucao_v1(arr.copy()), 1)
        self.assertEqual(solucao_v2(arr.copy()), 1)


    # Teste 4: propagação de carry parcial
    # 199 + 1 = 200
    def test_carry_parcial(self):
        arr = [1, 9, 9]

        self.assertEqual(solucao_v1(arr.copy()), 200)
        self.assertEqual(solucao_v2(arr.copy()), 200)

# =========================
# MENU PRINCIPAL
# =========================
if __name__ == "__main__":

    arr1 = [9, 9, 9]
    arr2 = [1, 2, 4]
    arr3 = [0]
    arr4 = [1, 9, 9]

    print("Digite 1 para usar a V1 (feita por mim)")
    print("Digite 2 para usar a V2 (refatorada por IA)")
    print("Digite 3 para executar testes unitários")
    op = int(input("Informe a opção desejada: "))

    if op == 1:
        print(f"Array: {arr1}")
        valMaj = solucao_v1(arr1)
        print(f"Valor +1: {valMaj}")

        print("\n=========================\n")

        print(f"Array: {arr2}")
        valMaj = solucao_v1(arr2)
        print(f"Valor +1: {valMaj}")

        print("\n=========================\n")

        print(f"Array: {arr3}")
        valMaj = solucao_v1(arr3)
        print(f"Valor +1: {valMaj}")

        print("\n=========================\n")

        print(f"Array: {arr4}")
        valMaj = solucao_v1(arr4)
        print(f"Valor +1: {valMaj}")

    elif op == 2:
        print(f"Array: {arr1}")
        valMaj = solucao_v2(arr1)
        print(f"Valor +1: {valMaj}")

        print("\n=========================\n")

        print(f"Array: {arr2}")
        valMaj = solucao_v2(arr2)
        print(f"Valor +1: {valMaj}")

        print("\n=========================\n")

        print(f"Array: {arr3}")
        valMaj = solucao_v2(arr3)
        print(f"Valor +1: {valMaj}")

        print("\n=========================\n")

        print(f"Array: {arr4}")
        valMaj = solucao_v2(arr4)
        print(f"Valor +1: {valMaj}")
    elif op == 3:
        unittest.main()
    else:
        print("Opção inválida.")