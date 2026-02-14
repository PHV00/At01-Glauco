"""
Atividade: Middle Node in a Linked List

Dado o head da lista vinculada isoladamente, encontre o nó do meio da lista vinculada.

Se o número de nós for ímpar, retorne o nó do meio.
Se o número de nós for par, existem dois nós do meio, então retorne o segundo nó do meio.

Fonte: https://www.geeksforgeeks.org/dsa/write-a-c-function-to-print-the-middle-of-the-linked-list/
"""

# Classe que representa cada nó da lista encadeada
class ListNode:
    def __init__(self, val=0, next=None):
        # Valor armazenado no nó
        self.val = val
        
        # Ponteiro que aponta para o próximo nó da lista
        self.next = next


def middleNode(head):
    # Ponteiro lento anda de 1 em 1 nó
    lento = head
    
    # Ponteiro rápido anda de 2 em 2 nós
    rapido = head

    # Enquanto o rápido não chegar no final da lista
    # e ainda existir próximo nó
    while rapido and rapido.next:
        
        # Lento avança um nó
        lento = lento.next
        
        # Rápido avança dois nós
        rapido = rapido.next.next

    # Quando o rápido chega ao final,
    # o lento estará exatamente no meio da lista
    return lento

# -------------------------------
# Criando manualmente a lista:
# 1 → 2 → 3 → 4 → 5
# -------------------------------

# Primeiro nó (head)
head = ListNode(1)

# Segundo nó
head.next = ListNode(2)

# Terceiro nó
head.next.next = ListNode(3)

# Quarto nó
head.next.next.next = ListNode(4)

# Quinto nó
head.next.next.next.next = ListNode(5)

# Chamando a função para encontrar o nó do meio
meio = middleNode(head)

# Imprimindo o valor do nó central
print(f"Nó central: {meio.val}")  # saída esperada: 3
