"""
-------------------------------------------------------------------------------------------------------------------------------------
Disciplina: Algoritmos Avançados   
Curso: Engenharia de Software  
Aluno(a): Amanda Korczagin
Professor: Glauco Scheffel
-------------------------------------------------------------------------------------------------------------------------------------

Problema: Nearest Smaller Vales (CSES)

-> Complexidade:
Tempo: 1s
Memória: 512MB

-> Estrutura principal utilizada:
Pilha, nível médio

-> Fonte do exercício:
https://cses.fi/problemset/task/3221/

-> Descrição do problema:
Dado um array de n números inteiros, para cada elemento deve-se encontrar o índice
do elemento anterior mais próximo que seja estrutamente menor que o atual.
Caso não exista, imprimir 0.

-> Estratégia V1 (feita por mim):
Utilizar uma pilha para armazenar índices dos elementos. Percorrer o array da esquerda para a direita.
Enquanto o topo da pilha for maior ou igual ao elemento atual, removemos da pilha. 
O topo restante será o elemento menor mais próximo. 

Entrada:
A primeira linha contém um inteiro n. 
A segunda linha contém n inteiros.

Saída:
Imprimir n inteiros representando o índice do menor elemento anterior para cada posição.

Restrições:
1 <= n <= 2 x 10^5
1 <= x_i <= 10^9

-> Justificativa da Estrutura:
A pilha é adequada porque o problema exige armazenamento temporário de elementos anteriores com a remoção
"eficiente" no padrão LIFO (Last in, first out).

"""

# V1 - Feito por mim 
def solve_v1():
    print("Digite o valor de n para a quantidade de números inteiros: ")

    try:
        n = int(input())
    except ValueError:
        print("Erro: n deve ser um número inteiro")
        return
    
    print("Digite os números separados por espaço: ")

    arr = list(map(int, input().split()))

    if len(arr) != n:
        print("Erro: quantidade de números diferente de n.")
        return
    
    #Armazenando índices
    pilha = []
    resultado = []

    for i in range(n):
        #Removendo valores maiores ou iguais ao atual
        while pilha and arr[pilha[-1]] >= arr[i]:
            pilha.pop()

        if not pilha:
            resultado.append(0)
        else:
            resultado.append(pilha[-1] +1)

        pilha.append(i)

    print("Resultado: ", *resultado)

"""
Seleção do uso de IA neste exercício

-> Prompt utilizado
"Estou desenvolvendo um problema encontrado no link https://cses.fi/problemset/task/3221/, Nearest Smaller Values.
Minha ideia é utilizar uma pilha para armazenar índices e remover elementos 
maiores até encontrar o menor anterior. 
O que você acha da minha hipótese para o problema? tem algo q poderia ser mais fácil?"

-> O que foi aproveitado
Confirmei minha estratégia de pilha, mas atualizei a organização estrutural.

-> O que foi adaptado:
Mantive a lógica principal desenvolvida, mas ajustei a organização e alguns comentários. 

-> Reflexão Final:
A IA foi utilizada como ferramenta de validação do solução proposta.

"""

# V2 - feito por IA
def solve_v2():
    print("Digite o valor de n e pressione Enter: ")

    try:
        n = int(input())
    except ValueError:
        print("Erro: n deve ser um número inteiro.")
        return

    print("Digite os números separados por espaço.")
    
    arr = []
    while len(arr) < n:
        try:
            arr.extend(map(int, input().split()))
        except ValueError:
            print("Erro: todos os valores devem ser inteiros.")
            return
        
    if len(arr) != n:
        print("Erro: quantidade incorreta de valores.")
        return
    
    stack = []
    resultado = [0] * n

    for i, valor in enumerate(arr):
        while stack and arr[stack[-1]] >= valor:
            stack.pop()

        resultado[i] = stack[-1] + 1 if stack else 0

        stack.append(i)
    
    print("Resultado: ", *resultado)

# Menu principal
if __name__ == "__main__":

    print("Digite 1 para executar a V1 (minha versão)")
    print("Digite 2 para executar a V2 (gerada por IA)")

    opcao = input("Escolha a opção: ")

    if opcao == "1":
        solve_v1()
    elif opcao == "2":
        solve_v2()
    else:
        print("Opção Inválida")