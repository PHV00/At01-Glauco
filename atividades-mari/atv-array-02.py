"""
-> Problema: Majority Element

-> Complexidade:
Tempo: O(n)
Memória: O(1)

-> Estrutura principal utilizada: Array - Nível médio

-> Descrição do problema:
Dado uma matriz arr[] de tamanho n, encontre o elemento que aparece mais de ⌊n/2⌋ (metade) vezes. 

-> Restrições:
Se não existir um elemento majoritário, retorne -1.

-> Estratégia V1:
Utilizei a função Counter de uma biblioteca externa, a qual retorna um dicionário com a contagem de cada item do array.
Percorri esse dicionário de contagem para tentar identificar se algum dos números tinha uma frequência > (tamanho_do_array/2).

Se sim, retorna esse número.
Se não, retorna -1.

-> Estratégia V2
Foi utilizado o algoritmo de votação de Boyer-Moore, que encontra o possível elemento majoritário percorrendo o array apenas uma vez, sem uso de estruturas auxiliares.
Isso ajuda a reduzir a memória de O(n) para O(1) mantendo tempo linear.

A ideia central é manter um candidato a majoritário e um contador de votos.

Sempre que o contador zera, o elemento atual passa a ser o novo candidato.
Quando o elemento atual é igual ao candidato, o contador é incrementado.
Quando é diferente, o contador é decrementado.

Essa lógica funciona porque o elemento majoritário aparece mais da metade das vezes, portanto não pode ser totalmente cancelado pelos demais valores.

Ao final do percurso, é feita uma verificação para confirmar se o candidato realmente é majoritário.
Caso não seja, retorna -1.

-> Entrada 1:
Array: [1, 1, 2, 1, 3, 5, 1]

-> Saída 1:
1

-> Entrada 2:
Array: [2, 13]

-> Saída 2:
-1

-> Utilização da IA
Neste exercício, a IA foi utilizada para refatorar o código e explicar sua refatoração linha a linha, de forma a facilitar a compreensão da nova lógica e
tornar o código mais eficiente utilizando python puro, sem bibliotecas externas.

-> Prompt

"dado o código abaixo, refatore e explique linha a linha com comentários

from collections import Counter
def solucao_v1(arr):
    metade = len(arr) // 2   # metade inteira
    contagem = Counter(arr)

    for numero, frequencia in contagem.items():
        if frequencia > metade:
            return numero

    return -1   # se não existir valor majoritário"

Fonte: https://www.geeksforgeeks.org/dsa/majority-element/
"""
# V1 - Feito por mim
from collections import Counter
def solucao_v1(arr):
    metade = len(arr) // 2   # metade inteira
    contagem = Counter(arr)

    for numero, frequencia in contagem.items():
        if frequencia > metade:
            return numero

    return -1   # se não existir valor majoritário

# V2 - Feito pela IA - Refatorado sem Counter e explicado linha a linha com comentários
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

# MENU PRINCIPAL
if __name__ == "__main__":

    arr1 = [1, 1, 2, 1, 3, 5, 1] # 1
    arr2 = [2, 13] # -1
    arr3 = [2, 2, 2, 4, 5, 1, 2, 3, 2, 5, 2] # 2
    arr4 = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3] # -1

    print("Digite 1 para usar a V1 (feita por mim)")
    print("Digite 2 para usar a V2 (refatorada por IA)")
    op = int(input("Informe a opção desejada: "))

    if op == 1:
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

    elif op == 2:
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
    else:
        print("Opção inválida.")
