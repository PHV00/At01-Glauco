"""
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

-> Entrada 1:
Lista de Nós: [1, 2, 3, 4, 5]

-> Saída 1:
3

-> Entrada 2:
Lista de Nós: [1, 2, 3, 4]

-> Saída 2:
3

-> Estratégia:
Temos dois ponteiros percorrendo a lista. Um deles avança de um em um, enquanto o outro avança de dois em dois.
Quando o que avança de dois em dois chegar ao final da lista, o que avança de um em um estará exatamente no meio.

-> Utilização da IA
Neste exercício, a IA foi utilizada para criar o rascunho do código e explicá-lo linha a linha, facilitando meu entendimento do problema. Depois, refatorei o código de forma a
deixá-lo mais organizado dado o contexto da atividade. Além disso, ela também foi utilizada para criar novos casos de teste além daqueles que constam no site.

-> Prompt
"dado o seguinte problema, resolva em python e me explique o passo a passo

Given the head of singly linked list, find middle node of the linked list.

If the number of nodes is odd, return the middle node.
If the number of nodes is even, there are two middle nodes, so return the second middle node."

Fonte: https://www.geeksforgeeks.org/dsa/write-a-c-function-to-print-the-middle-of-the-linked-list/
"""

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

# MENU PRINCIPAL
if __name__ == "__main__":
    print("1 - Lista 5 nós (ÍMPAR)")
    print("2 - Lista 6 nós (PAR)")
    print("3 - Lista com 1 nó")
    print("4 - Lista com 2 nós")

    op = int(input("Informe a opção desejada: "))

    if op == 1:
        head = createOddList()
    elif op == 2:
        head = createEvenList()
    elif op == 3:
        head = createSingleNodeList()
    elif op == 4:
        head = createTwoNodeList()
    else:
        print("Opção inválida.")
        exit()

    meio = middleNode(head)
    print(f"Nó central: {meio.val}")