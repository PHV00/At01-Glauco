"""
-------------------------------------------------------------------------------------------------------------------------------------
Disciplina: Algoritmos Avançados   
Curso: Engenharia de Software  
Aluno(a): Amanda Korczagin
Professor: Glauco Scheffel
-------------------------------------------------------------------------------------------------------------------------------------

Problema: List Removals (CSES)

-> Complexidade:
Tempo: 1s
Memória: 512MB

-> Estrutura principal utilizada:
Lista Encadeada, nível médio.

-> Fonte do exercício:
https://cses.fi/problemset/task/1749/

-> Descrição do problema:
Dado um array com n elementos, você deve remover os elementos um por um de acordo com 
as posições fornecidas. Após cada remoção, imprimir valor removido. 

-> Estratégia V1 (feita por mim):
Simular uma lista encadeada onde cada nó aponta para o próximo.
Para cada posição informada, percorreria a lista até a posição desejada, removendo o nó e
ajustando os ponteiros. No final, imprimir o valor que foi removido.

Entrada:
A primeira linha contém um inteiro n.
A segunda linha contém os n valores inteiros da lista.
A terceita linha contém n posições de números inteiros a serem removidos.

Saída:
Imprimir os valores removidos na ordem das operações.

Restrições:
1 <= n <= 2 x 10^5
1 <= valores <= 10^9
1 <= posição <= tamanho atual da lista

-> Justificativa da estrutura:
A lista encadeada se encaixa no problema, pois permite uma remoção "dinâmica" dos elementos.

"""

# V1 - feita por mim

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def solve_v1():

    print("Digite o valor de elementos da lista: ")
    try:
        n = int(input())
    except ValueError:
        print("Erro: o número indicado deve ser um inteiro")
        return
    
    print("Digite os valores da lista: ")
    values = list(map(int, input().split()))

    print("Digite as posições de remoção: ")
    positions = list(map(int, input().split()))

    if len(values) != n or len(positions) != n:
        print("Erro: quantidade incorreta de elementos adicionados.")
        return
    
    #Construindo a lista encadeada
    head = Node(values[0])
    current = head

    for v in values[1:]:
        current.next = Node(v)
        current = current.next

    resultado = []

    for pos in positions:
        prev = None
        current = head

        #Indo até a posição desejada
        for _ in range(pos -1):
            prev = current
            current = current.next

        resultado.append(current.value)

        #Removendo o nó
        if prev is None:
            head = current.next
        else:
            prev.next = current.next

    print("Ordem de remoção: ", *resultado)

"""

Seleção do uso de IA nesta atividade

-> Prompt utilizado:
"Etou resolvendo o problema List Removals do CSES, do link "https://cses.fi/problemset/task/1749/"
Minha ideia é utilizar uma lista encadeada para remover os elementos ordenadamente. 
Segue em anexo o código que utilizei e o print do teste no terminal.
O que você achou? podemos simplificar o problema?

-> O que foi aproveitado:
Confirmei a utilização da lista encadeada para resolução do problema e confirmei a lógica de remoção "dinâmica"

-> O que foi adaptado:
Reestruturei a organização do código e adicionei validações na entrada.

-> Reflexão final:
A IA foi utilizada como ferramenta de validação estrutural e de organização do código. 

"""

# V2 - feita pela IA

def solve_v2():
    print("Digite o valor de n: ")
    try:
        n = int(input())
    except ValueError:
        print("Erro: n deve ser um número inteiro")
        return
    
    print("Digite os valores da lista: ")
    try:
        values = list(map(int, input().split()))
    except ValueError:
        print("Erro: todos os valores devem ser números inteiros.")
        return
    
    print("Digite as posições de remoção: ")
    try:
        positions = list(map(int, input().split()))
    except ValueError:
        print("Erro: posições devem ser inteiras.")
        return
    
    if len(values) != n or len(positions) != n:
        print("Erro: quantidade incorreta de dados.")
        return
    
    resultado = []

    #Simulação com a lista dinâmica
    for pos in positions:
        removido = values.pop(pos-1)
        resultado.append(removido)

    print("Ordem de remoção ", *resultado)



# Menu principal

if __name__ == "__main__":
    print("Digite 1 para executar a V1 (minha versão)")
    print("Digite 2 para executar a V2 (versão da IA)")

    opcao = input("Escolha a opção: ")

    if opcao == "1":
        solve_v1()
    elif opcao == "2":
        solve_v2()
    else:
        print("Opção Inválida.")