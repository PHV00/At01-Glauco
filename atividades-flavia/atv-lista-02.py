"""
-------------------------------------------------------------------------------------------------------------------------------------
Disciplina: Algoritmos Avançados   
Curso: Engenharia de Software  
Aluno(a): Flavia Antonieli de Souza 
Professor: Glauco Scheffel
-------------------------------------------------------------------------------------------------------------------------------------

Problema: Josephus Problem I (CSES)

-> Complexidade:
Tempo: 1.00 s | O(n)
Memória: 512 MB | O(n)

-> Estrutura principal utilizada:
Lista Encadeada (simulada com deque)

-> Descrição:
Existem n crianças numeradas de 1 até n, dispostas em círculo.
Durante a brincadeira, remove-se uma criança sim, uma não,
até que nenhuma reste.

A tarefa é imprimir a ordem de remoção.

Entrada:
Um único inteiro n.

Saída:
A ordem de remoção das crianças.

Restrições:
1 ≤ n ≤ 2 x 10⁵

Exemplo:

Entrada:
7

Saída:
2 4 6 1 5 3 7

Fonte:
https://cses.fi/problemset/task/2162/
"""

from collections import deque

# V1 - Minha versão

def solve_v1():
    print("Digite o valor da quantidade de crianças <pressione Enter> :")

    try:
        n = int(input())
    except ValueError:
        print("Erro: número deve ser inteiro.")
        return

    # Teste de usuário
    if n < 0:
        print("Erro: número não pode ser negativo.")
        return

    if n == 0:
        print("Caso especial identificado: número = 0")
        print("Ordem de remoção: (vazio)")
        return

    children = deque(range(1, n + 1))
    result = []

    while children:
        # Pula uma criança
        children.append(children.popleft())

        # Remove a próxima
        result.append(children.popleft())

    print("Ordem de remoção:")
    print(*result)

    # Teste Matemático
    print("\n--- Teste Matemático ---")

    if len(result) == n:
        print("✔ Todas as crianças foram removidas corretamente.")
    else:
        print("✘ Erro: quantidade incorreta de remoções.")

    if sorted(result) == list(range(1, n + 1)):
        print("✔ Nenhuma criança foi repetida ou perdida.")
    else:
        print("✘ Erro: há repetição ou perda de elementos.")


# V2 - Refatorada pela IA

"""
Seção: Uso de IA nesta atividade

-> Prompt utilizado:
"Estou resolvendo o problema Josephus Problem I do CSES em Python.
Preciso remover uma criança sim, uma não, em formato circular.
Qual é a melhor estrutura para simular isso com eficiência?
A complexidade está adequada para n até 2 X 10⁵?"

-> O que foi aproveitado:
- Sugestão de utilizar deque para simular estrutura circular.

-> O que foi adaptado:
- Mantivemos V1 independente.
- Organizamos melhor a estrutura da solução.

-> Reflexão:
A IA auxiliou na escolha da estrutura adequada para simular
o comportamento circular de forma eficiente.
"""

def solve_v2():
    print("Digite o valor da quantidade de crianças <pressione Enter> :")

    try:
        n = int(input())
    except ValueError:
        print("Erro: número deve ser inteiro.")
        return
# ------------------------------
# Teste de usuário
# ------------------------------

    if n < 0:
        print("Erro: número não pode ser negativo.")
        return

    if n == 0:
        print("Caso especial identificado: número = 0")
        print("Ordem de remoção: (vazio)")
        return

    children = deque(range(1, n + 1))
    removal_order = []

    while children:
        # Rotaciona (pula 1)
        children.rotate(-1)

        # Remove atual
        removal_order.append(children.popleft())

    print("Ordem de remoção:")
    print(*removal_order)

# ------------------------------
# Teste Matemático
# ------------------------------
    print("\n--- Teste Matemático ---")

    if len(removal_order) == n:
        print("✔ Todas as crianças foram removidas corretamente.")
    else:
        print("✘ Erro: quantidade incorreta de remoções.")

    if sorted(removal_order) == list(range(1, n + 1)):
        print("✔ Nenhuma criança foi repetida ou perdida.")
    else:
        print("✘ Erro: há repetição ou perda de elementos.")


# MENU PRINCIPAL

if __name__ == "__main__":

    print("Digite 1 para executar V1 (minha versão)")
    print("Digite 2 para executar V2 (refatorada pela IA)")

    escolha = input("Escolha a opção: ")

    if escolha == "1":
        solve_v1()
    elif escolha == "2":
        solve_v2()
    else:
        print("Opção inválida.")
