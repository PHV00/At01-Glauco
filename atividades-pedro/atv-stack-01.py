"""
-------------------------------------------------------------------------------------------------------------------------------------
Disciplina: Algoritmos Avançados   
Curso: Engenharia de Software  
Aluno(a): Pedro Henrique Vitoreti
Professor: Glauco Scheffel
-------------------------------------------------------------------------------------------------------------------------------------
Nome do problema : Queue using two Stacks
Link do problema : https://www.geeksforgeeks.org/problems/queue-using-two-stacks/1?utm_source=chatgpt.com
Link Artigo associado ao problema : https://www.geeksforgeeks.org/dsa/how-to-identify-and-solve-monotonic-stack-problems/
Plataforma utilizada : GeeksforGeeks 
Estrutura de dados principal usada : 
Justificativa:
Dificuldade: Media
-------------------------------------------------------------------------------------------------------------------------------------
"""

"""
PROBLEMA:Implemente uma fila usando duas pilhas, s1 e s2.

Uma consulta q pode ser de dois tipos:
(i) 1 x (uma consulta desse tipo significa inserir 'x' na fila)
(ii) 2 (uma consulta desse tipo significa remover um elemento da fila e imprimir o elemento removido)

Observação: Se não houver nenhum elemento, retorne -1 como resposta ao remover um elemento.

Exemplos:

Entrada: q=5, queries[][]=[[1, 2], [1, 3], [2], [1, 4], [2]]
Saída: [2, 3]
Explicação:
No primeiro caso de teste,
[1 2] a fila será [2]
[1 3] a fila será [2 3]
[2] o elemento removido será 2 e a fila será [3]
[1 4] a fila será [3 4]
[2] o elemento removido será 3.

Entrada: q = 4, queries[][] = [[1, 2], [2], [2], [1, 4]]
Saída: [2, -1]
Explicação:
No segundo caso de teste,
[1, 2] a fila será [2]
[2] o elemento removido será [2] e

então a fila estará vazia
[2] o A fila está vazia e, portanto, -1
[1, 4] a fila será [4].

Restrições:
1 <= q <= 100
1 <= x <= 100

"""

# V1 - Método Feita por mim
class StacksLikeList:
    def __init__(self):
        self.stackA = []
        self.stackB = []

    def enqueue(self, x):
        self.stackA.append(x)

    def dequeue(self):
        if len(self.stackB) == 0:
            while self.stackA:
                self.stackB.append(self.stackA.pop())

        if len(self.stackB) == 0:
            return -1

        return self.stackB.pop()

    def process_query(self, query):
        if query[0] == 1:
            self.enqueue(query[1])
            return

        elif query[0] == 2:
            return self.dequeue()

# v2 - Método Feita pela IA
"""
PROMPT: Estou resolvendo o problema Queue using two Stacks do geeksforgeeks em Python (https://www.geeksforgeeks.org/problems/queue-using-two-stacks/1?utm_source=chatgpt.com).
dado este codigo de resolução: 
class StacksLikeList:
    def __init__(self):
        self.stackA = []
        self.stackB = []

    def enqueue(self, x):
        self.stackA.append(x)

    def dequeue(self):
        if len(self.stackB) == 0:
            while self.stackA:
                self.stackB.append(self.stackA.pop())

        if len(self.stackB) == 0:
            return -1

        return self.stackB.pop()

    def process_query(self, query):
        if query[0] == 1:
            self.enqueue(query[1])
            return

        elif query[0] == 2:
            return self.dequeue()

Me explique quais os melhores metodos e logicas para resolver este problema, trazendo com isso os
respectivos codigos e explicando as mudanças e melhorias em relação ao código acima e
o porque e oque estas mudanças afetam, de preferencia com metricas de tempo e processamento.
"""

from collections import deque

class Queue:
    def __init__(self):
        self.q = deque()

    def process_query(self, query):
        if query[0] == 1:
            self.q.append(query[1])
        else:
            return self.q.popleft() if self.q else -1

# Testes dos metodos
if __name__ == "__main__":
    # Teste do método V1
    q = StacksLikeList()

    q.enqueue(2)
    q.enqueue(3)
    
    print("********HUMANO*******")
    print(q.stackA)  # [2, 3]
    print(q.stackB)  # []
    print("***************")

    # Teste do método V2
    q = Queue()

    q.process_query([1, 2])  # inserir 2
    q.process_query([1, 3])  # inserir 3

    print("********IA*******")
    print(list(q.q))  # [2, 3]
    print("***************")