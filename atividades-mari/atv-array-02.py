"""
-------------------------------------------------------------------------------------------------------------------------------------
Disciplina: Algoritmos Avançados   
Curso: Engenharia de Software  
Aluno(a): Marina Rosa Oliveira
Professor: Glauco Scheffel
-------------------------------------------------------------------------------------------------------------------------------------

Problema: Majority Element

-> Complexidade:
Tempo: O(n)
Memória: O(1)

-> Estrutura principal utilizada: Array - Nível médio

-> Descrição do problema:
Dada uma matriz arr[] de tamanho n, encontre o elemento que aparece mais de ⌊n/2⌋ (metade) vezes. 

-> Restrições:
Se não existir um elemento majoritário, retorne -1.

-> Utilização da IA
Neste exercício, a IA foi utilizada para refatorar o código e explicar sua refatoração linha a linha, de forma a facilitar a compreensão da nova lógica e
tornar o código mais eficiente utilizando python puro, sem bibliotecas externas.

Fonte: https://www.geeksforgeeks.org/dsa/majority-element/
"""
# V1 - Feito por mim
from collections import Counter
import unittest

def solucao_v1(arr):
    metade = len(arr) // 2   # metade inteira
    contagem = Counter(arr)

    for numero, frequencia in contagem.items():
        if frequencia > metade:
            return numero

    return -1   # se não existir valor majoritário

# V2 - Refatorado pela IA
def solucao_v2(arr):

    # Candidato a possível elemento majoritário
    candidato = None

    # Contador que representa a "vantagem" do candidato atual
    cont = 0

    for num in arr:
        # Se o contador chegou a zero,
        # significa que o candidato anterior foi neutralizado
        # então escolhemos um novo candidato
        if cont == 0:
            candidato = num

        # Se o número atual for igual ao candidato,
        # aumentamos sua vantagem (voto positivo)
        if num == candidato:
            cont += 1
        else:
            # Se for diferente, diminuímos sua vantagem (voto negativo)
            cont -= 1

    # Após percorrer o array, temos um possível candidato.
    # Agora precisamos confirmar se ele aparece mais da metade das vezes
    if arr.count(candidato) > len(arr) // 2:
        return candidato

    # Caso não exista elemento majoritário
    return -1

# =========================
# TESTES UNITÁRIOS
# =========================

class TestMajorityElement(unittest.TestCase):

    # Teste 1: existe elemento majoritário
    def test_array_com_majoritario(self):
        arr = [1, 1, 2, 1, 3, 5, 1]
        self.assertEqual(solucao_v1(arr), 1)
        self.assertEqual(solucao_v2(arr), 1)

    # Teste 2: não existe elemento majoritário
    def test_array_sem_majoritario(self):
        arr = [1, 2, 3, 4]
        self.assertEqual(solucao_v1(arr), -1)
        self.assertEqual(solucao_v2(arr), -1)

# =========================
# MENU PRINCIPAL
# =========================
if __name__ == "__main__":

    arr1 = [1, 1, 2, 1, 3, 5, 1] # 1
    arr2 = [2, 13] # -1
    arr3 = [2, 2, 2, 4, 5, 1, 2, 3, 2, 5, 2] # 2
    arr4 = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3] # -1

    print("Digite 1 para usar a V1 (feita por mim)")
    print("Digite 2 para usar a V2 (refatorada por IA)")
    print("Digite 3 para executar os testes unitários.")
    op = int(input("Informe a opção desejada: "))

    if op == 1: # V1
        print(f"Array: {arr1}")
        valMaj = solucao_v1(arr1)
        print(f"Valor majoritário: {valMaj}")

        print("\n=========================\n")

        print(f"Array: {arr2}")
        valMaj = solucao_v1(arr2)
        print(f"Valor majoritário: {valMaj}")

        print("\n=========================\n")

        print(f"Array: {arr3}")
        valMaj = solucao_v1(arr3)
        print(f"Valor majoritário: {valMaj}")

        print("\n=========================\n")

        print(f"Array: {arr4}")
        valMaj = solucao_v1(arr4)
        print(f"Valor majoritário: {valMaj}")

    elif op == 2: # V2
        print(f"Array: {arr1}")
        valMaj = solucao_v2(arr1)
        print(f"Valor majoritário: {valMaj}")

        print("\n=========================\n")

        print(f"Array: {arr2}")
        valMaj = solucao_v2(arr2)
        print(f"Valor majoritário: {valMaj}")

        print("\n=========================\n")

        print(f"Array: {arr3}")
        valMaj = solucao_v2(arr3)
        print(f"Valor majoritário: {valMaj}")

        print("\n=========================\n")

        print(f"Array: {arr4}")
        valMaj = solucao_v2(arr4)
        print(f"Valor majoritário: {valMaj}")

    elif op == 3: # Testes
        unittest.main()
    else:
        print("Opção inválida.")
