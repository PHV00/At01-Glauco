"""
Atividade: Elemento Maioria

Dado uma matriz arr[] de tamanho n, encontre o elemento que aparece mais de ⌊n/2⌋ (metade) vezes. Se não existir tal elemento, retorne -1.

Fonte: https://www.geeksforgeeks.org/dsa/majority-element/
"""
# V1 - Feito por mim
from collections import Counter

def identificar_valor_majoritario(arr):
    metade = len(arr) // 2   # metade inteira
    contagem = Counter(arr)

    for numero, frequencia in contagem.items():
        if frequencia > metade:
            return numero

    return -1   # se não existir valor majoritário


# Deve retornar 2
arr = [1, 2, 2, 2, 2, 5, 1]

# Deve retornar -1
# arr = [1, 2, 3]

print(identificar_valor_majoritario(arr))

# V2 - Feito pela IA - Refatorado sem Counter e explicado linha a linha com comentários
# def identificar_valor_majoritario(arr):
    
#     # Variável que vai guardar o possível valor majoritário
#     candidato = None

#     # Contador que controla o "saldo de votos" do candidato
#     cont = 0

#     # Percorre todos os elementos do array
#     for num in arr:
        
#         # Se o contador zerar, escolhemos um novo candidato
#         if cont == 0:
#             candidato = num
        
#         # Se o número atual for igual ao candidato,
#         # incrementa o contador (ganha um voto)
#         # Caso contrário, decrementa (perde um voto)
#         cont += 1 if num == candidato else -1

#     # Após o loop, o candidato pode ou não ser majoritário,
#     # então fazemos uma verificação final contando ocorrências
#     if arr.count(candidato) > len(arr) // 2:
#         return candidato

#     # Se não for majoritário, retorna -1
#     return -1

# # Retorna 1
# #print(identificar_valor_majoritario([1, 1, 2, 1, 3, 5, 1]))

# # Retorna -1
# print(identificar_valor_majoritario([1, 2, 3]))



    
