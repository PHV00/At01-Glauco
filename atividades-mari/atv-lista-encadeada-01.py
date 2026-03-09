"""
-------------------------------------------------------------------------------------------------------------------------------------
Disciplina: Algoritmos Avançados   
Curso: Engenharia de Software  
Aluno(a): Marina Rosa Oliveira
Professor: Glauco Scheffel
-------------------------------------------------------------------------------------------------------------------------------------

-> Problema: Middle Node in a Linked List

-> Complexidade: 
Tempo: O(n)
Memória: O(1)

-> Estrutura principal utilizada: Lista Encadeada - Nível fácil

-> Descrição do problema: Dado o head da lista vinculada isoladamente, encontre o nó do meio da lista vinculada.

Se o número de nós for ímpar, retorne o nó do meio.
Se o número de nós for par, existem dois nós do meio, então retorne o segundo nó do meio.

-> Restrições:
Caso a lista tenha uma quantidade par de registros, deve ser retornado o "segundo do meio".

-> Utilização da IA
Neste exercício, a IA foi utilizada para criar o rascunho do código e explicá-lo linha a linha, facilitando meu entendimento do problema. Depois, refatorei o código de forma a
deixá-lo mais organizado dado o contexto da atividade. Além disso, ela também foi utilizada para criar novos casos de teste além daqueles que constam no site.

Fonte: https://www.geeksforgeeks.org/dsa/write-a-c-function-to-print-the-middle-of-the-linked-list/
"""

import unittest

# Classe que representa cada nó da lista encadeada
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def middleNode(head):
    # Ponteiro lento anda de 1 em 1 nó
    lento = head
    
    # Ponteiro rápido anda de 2 em 2 nós
    rapido = head

    # Enquanto o rápido não chegar no final da lista
    # e ainda existir próximo nó
    while rapido and rapido.next:
        # Ponteiros avançam em suas respectivas velocidades
        lento = lento.next
        rapido = rapido.next.next

    return lento

# -------------------------------
# Criando manualmente a lista:
# -------------------------------

def createOddList():
    # Primeiro nó (head)
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    return head

def createEvenList():
    # Primeiro nó (head)
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)

    return head

def createSingleNodeList():
    return ListNode(10)

def createTwoNodeList():
    head = ListNode(7)
    head.next = ListNode(8)
    return head

# =========================
# TESTES UNITÁRIOS
# =========================
class TestMiddleNode(unittest.TestCase):

    # Função auxiliar para criar uma linked list a partir de uma lista
    def criar_lista(self, valores):

        head = ListNode(valores[0])
        atual = head

        for v in valores[1:]:
            atual.next = ListNode(v)
            atual = atual.next

        return head


    # Teste 1: número ímpar de nós
    def test_lista_impar(self):

        head = self.criar_lista([1, 2, 3, 4, 5])

        meio = middleNode(head)

        self.assertEqual(meio.val, 3)


    # Teste 2: número par de nós (deve retornar o segundo meio)
    def test_lista_par(self):

        head = self.criar_lista([1, 2, 3, 4, 5, 6])

        meio = middleNode(head)

        self.assertEqual(meio.val, 4)


    # Teste 3: lista com apenas um elemento
    def test_lista_um_elemento(self):

        head = self.criar_lista([10])

        meio = middleNode(head)

        self.assertEqual(meio.val, 10)


    # Teste 4: lista com dois elementos
    def test_lista_dois_elementos(self):

        head = self.criar_lista([7, 8])

        meio = middleNode(head)

        self.assertEqual(meio.val, 8)

# =========================
# MENU PRINCIPAL
# =========================
if __name__ == "__main__":
    print("1 - Lista 5 nós (ÍMPAR)")
    print("2 - Lista 6 nós (PAR)")
    print("3 - Lista com 1 nó")
    print("4 - Lista com 2 nós")
    print("5 - Executar testes unitários")

    op = int(input("Informe a opção desejada: "))

    if op == 1:
        head = createOddList()
    elif op == 2:
        head = createEvenList()
    elif op == 3:
        head = createSingleNodeList()
    elif op == 4:
        head = createTwoNodeList()
    elif op == 5:
        unittest.main()
    else:
        print("Opção inválida.")
        exit()

    meio = middleNode(head)
    print(f"Nó central: {meio.val}")