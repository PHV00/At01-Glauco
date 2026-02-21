"""
-------------------------------------------------------------------------------------------------------------------------------------
Disciplina: Algoritmos Avançados   
Curso: Engenharia de Software  
Aluno(a): Pedro Henrique Vitoreti
Professor: Glauco Scheffel
-------------------------------------------------------------------------------------------------------------------------------------
Nome do problema : Detect Loop in linked list
Link do problema : https://www.geeksforgeeks.org/problems/detect-loop-in-linked-list/0?utm_source=chatgpt.com
Plataforma utilizada : GeeksforGeeks 
Estrutura de dados principal usada : lista encadeada sem loop
Justificativa: Foi gerado dois metodos para validar se uma lista encadeade está em loop ou não,
o primeiro método utiliza um set para armazenar os nós visitados, enquanto o segunto método utiliza 
o algoritmo de Floyd's Tortoise and Hare, que é mais eficiente para detectar ciclos 
em listas encadeadas.Assim solucionando o problema que era indetificar quando um loop ocorria.
-------------------------------------------------------------------------------------------------------------------------------------
"""
"""
PROBLEMA: Você recebe o primeiro nó de uma lista simplesmente encadeada.
Você precisa determinar se a lista encadeada contém um loop ou não.
Um loop existe em uma lista encadeada se o ponteiro `next` do último nó 
apontar para qualquer outro nó da lista (incluindo ele mesmo), em vez de ser nulo.

Nota: Internamente, `pos` (índice baseado em 1) é usado para denotar
a posição do nó ao qual o ponteiro `next` do último nó está conectado.
Se `pos = 0`, significa que o último nó aponta para `null`. 
Observe que `pos` não é passado como parâmetro.
"""
# Estrutura base emulando um nó em uma lista encadeada por meio das classes em python 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def print_list(self, limit=20):

        current = self.head
        count = 0

        while current and count < limit:
            print(current.data)
            current = current.next
            count += 1


# V1 - Método Feita por mim
def detect_loop_set(head):
    visited = set()
    current = head

    while current:
        if current in visited:
            return True

        visited.add(current)
        current = current.next

    return False

# V2 - Método Feita com IA
"""
PROMPT: Estou resolvendo o problema Detect Loop in linked list do geeksforgeeks em Python (https://www.geeksforgeeks.org/problems/detect-loop-in-linked-list/0?utm_source=chatgpt.com).
dado este codigo de resolução: 
def detect_loop_set(head):
    visited = set()
    current = head

    while current:
        if current in visited:
            return True

        visited.add(current)
        current = current.next

    return False
Me explique quais os melhores metodos e logicas para resolver este problema, trazendo com isso os
respectivos codigos e explicando as mudanças e melhorias em relação ao código acima e
o porque e oque estas mudanças afetam, de preferenciam com metricas de tempo e processamento.
"""
def detect_loop_floyd(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow is fast:
            return True

    return False


# Teste dos métodos

if __name__ == "__main__":
    # Lista encadeada com um loop
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)

    ll.head.next.next.next.next = ll.head.next

    print("Detectando loop usando set: ", detect_loop_set(ll.head))  
    print("Detectando loop usando Floyd: ", detect_loop_floyd(ll.head))

    # Lista encadeada sem loop
    ll2 = LinkedList()
    ll2.append(1)
    ll2.append(2)
    ll2.append(3)
    ll2.append(4)

    print("Detectando loop usando set: ", detect_loop_set(ll2.head))  
    print("Detectando loop usando Floyd's Tortoise and Hare: ", detect_loop_floyd(ll2.head)) 
