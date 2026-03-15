"""
-------------------------------------------------------------------------------------------------------------------------------------
Disciplina: Algoritmos Avançados   
Curso: Engenharia de Software  
Aluno(a): Flavia Antonieli de Souza 
Professor: Glauco Scheffel
-------------------------------------------------------------------------------------------------------------------------------------

Problema: Repetitions (CSES)

-> Estrutura principal utilizada:
Pilha

-> Complexidade:
Tempo: O(n) 
Memória: O(n)

-> Descrição:
Dada uma sequência de DNA composta por A, C, G e T,
determinar o comprimento da maior repetição consecutiva
de um único caractere utilizando estrutura de Pilha.

Entrada
A única linha de entrada contém uma string denpersonagens.

Saída
Imprima um número inteiro: o comprimento da repetição mais longa.

Restrições
1 ≤ n ≤ 10^6

Exemplo

Entrada:
ATTCGGGA

Saída:
3

fonte:https://cses.fi/problemset/task/1069/  

"""

# V1 - Minha versão

def solve_v1():
    print("Digite a sequência de DNA <pressione Enter> :")
    print("Use apenas as letras A (Adenina), C (Citosina), G (Guanina), T (Timina).")

    dna = input().strip()

    if not dna:
        print("Erro: sequência vazia.")
        return

    dna = dna.upper()

    allowed = {"A", "C", "G", "T"}

    for char in dna:
        if char not in allowed:
            print("Erro: sequência inválida.")
            print("Use apenas as letras A, C, G ou T.")
            return

    stack = []
    max_count = 0

    for char in dna:
        if stack and stack[-1][0] == char:
            last_char, count = stack.pop()
            count += 1
            stack.append((char, count))
        else:
            stack.append((char, 1))

        max_count = max(max_count, stack[-1][1])

    print("Maior repetição consecutiva:", max_count)

    # Teste Matemático
    print("\n--- Teste Matemático ---")
    if 1 <= max_count <= len(dna):
        print("✔ Resultado consistente.")
    else:
        print("✘ Resultado inconsistente.")


# V2 - Refatorada pela IA 

"""
Seção: Uso de IA nesta atividade

-> Prompt utilizado:
"Preciso resolver o problema Repetitions do CSES
utilizando estrutura de Pilha.
Como organizar melhor a lógica para tornar o código
mais modular e estruturado?"

-> O que foi aproveitado:
- Separação da lógica em função auxiliar.
- Organização mais limpa do fluxo.
- Atualização direta do topo da pilha.

-> O que foi adaptado:
- Mantivemos V1 independente.
- Modularizamos a lógica da pilha.
- Melhoramos a validação de entrada.

-> Reflexão:
A IA auxiliou na reorganização estrutural da solução,
tornando o código mais modular e reutilizável.
"""

def calcular_maior_repeticao(dna):
    stack = []
    max_streak = 0

    for char in dna:
        if not stack:
            stack.append((char, 1))
        elif stack[-1][0] == char:
            topo_char, topo_count = stack[-1]
            stack[-1] = (topo_char, topo_count + 1)
        else:
            stack.append((char, 1))

        max_streak = max(max_streak, stack[-1][1])

    return max_streak


def solve_v2():
    print("Digite a sequência de DNA <pressione Enter> :")
    print("Use apenas as letras A, C, G ou T (maiúsculas ou minúsculas).")

    dna = input().strip()

    if not dna:
        print("Erro: sequência vazia.")
        return

    dna = dna.upper()

    if any(char not in "ACGT" for char in dna):
        print("Erro: sequência inválida.")
        print("Use apenas as letras A, C, G ou T.")
        return

    resultado = calcular_maior_repeticao(dna)

    print("Maior repetição consecutiva:", resultado)

    # Teste Matemático
    print("\n--- Teste Matemático ---")
    if 1 <= resultado <= len(dna):
        print("✔ Resultado consistente.")
    else:
        print("✘ Resultado inconsistente.")


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
