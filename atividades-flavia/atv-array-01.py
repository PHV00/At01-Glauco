"""
-------------------------------------------------------------------------------------------------------------------------------------
Disciplina: Algoritmos Avançados   
Curso: Engenharia de Software  
Aluno(a): Flavia Antonieli de Souza 
Professor: Glauco Scheffel
-------------------------------------------------------------------------------------------------------------------------------------

Problema: Increasing Array (CSES)

-> Complexidade:
Tempo: 1.00 s | O(n)
Memória: 512 MB | O(1)

-> Estrutura principal utilizada: Array - Nível fácil

-> Descrição do problema:
Você recebe um array de n inteiros. Você quer modificar o array para que ele aumente, ou seja, 
cada elemento seja pelo menos tão grande quanto o elemento anterior.
A cada movimento, você pode aumentar o valor de qualquer elemento em um. 
Qual é o número mínimo de movimentos necessários?

Entrada:
A primeira linha contém um inteiro n: o tamanho do array.
A segunda linha contém n inteiros x₁, x₂, ..., xₙ: os elementos do array.

Saída:
Imprima um único inteiro: o número mínimo de movimentos necessários.

Restrições:
1 ≤ n ≤ 2 x 10⁵
1 ≤ xᵢ ≤ 10⁹

Exemplo:

Entrada:
5
3 2 5 1 7

Saída:
5

-> Justificativa da estrutura:
O array é adequado porque o problema exige acesso sequencial
aos elementos e comparação entre posições adjacentes,
sem necessidade de inserções ou remoções.

-> Estratégia:
Percorrer o array da esquerda para a direita,
mantendo o maior valor já visto.
Se o valor atual for menor que o anterior,
somamos a diferença ao contador.

-> Fonte: https://cses.fi/problemset/task/1094/
"""

# V1 - Minha versão 

def solve_v1():
    print("Digite o valor de n e <pressione Enter> :")
    n = int(input())

    # Validação: n igual a 0 (teste 01)
    if n == 0:
        print("\nCaso especial identificado: n = 0")
        print("Número mínimo de incrementos: 0")
        return

    print(f"Digite os {n} números separados por espaço e <pressione Enter> :")
    arr = list(map(int, input().split()))

    # Validação: quantidade incorreta de números (teste 02)
    if len(arr) != n:
        print("\nErro: a quantidade de números digitados não corresponde ao valor de n.")
        print(f"n informado: {n}")
        print(f"Quantidade digitada: {len(arr)}")
        return

    moves = 0
    previous = arr[0]

    for i in range(1, n):
        if arr[i] < previous:
            moves += previous - arr[i]
        else:
            previous = arr[i]

    print("Número mínimo de incrementos:", moves)


# V2 - Refatorada pela IA 

"""
Seção: Uso de IA nesta atividade

-> Prompt utilizado:
"Estou resolvendo o problema Increasing Array do CSES em Python
(https://cses.fi/problemset/task/1094/).
Minha ideia é percorrer o array apenas uma vez, comparando cada elemento
com o anterior para garantir que ele seja não-decrescente.
Essa estratégia está correta?
A complexidade é adequada para as restrições do problema?
Você pode me mostrar uma versão mais organizada ou refatorada do código?"

-> O que foi aproveitado:
- Confirmação de que percorrer o array uma única vez resolve o problema.
- Validação de que a complexidade O(n) é adequada para n ≤ 2x10⁵.
- Sugestões para organizar melhor a estrutura do código.

-> O que foi adaptado:
- Mantivemos nossa implementação original como V1.
- Reescrevemos a V2 de forma independente, aplicando melhorias estruturais.

-> Reflexão:
A IA foi utilizada como ferramenta de apoio para validar a lógica proposta
e melhorar a organização da solução. A estratégia principal já havia sido
pensada, e as adaptações realizadas demonstram compreensão do
algoritmo e das restrições do problema.
"""

# V2 - Refatorada pela IA 

def solve_v2():
    print("Digite o valor de n e pressione Enter:")
    
    try:
        n = int(input())
    except ValueError:
        print("Erro: n deve ser um número inteiro.")
        return

# ------------------------------
# Validação: n igual a 0
# ------------------------------
    if n == 0:
        print("\nCaso especial identificado: n = 0")
        print("Número mínimo de incrementos: 0")
        return

    print(f"Digite os {n} números separados por espaço e pressione Enter:")

    # Leitura robusta: continua lendo até atingir n números
    arr = []
    while len(arr) < n:
        try:
            arr.extend(map(int, input().split()))
        except ValueError:
            print("Erro: todos os valores devem ser inteiros.")
            return

# ------------------------------
# Validação: quantidade incorreta
# ------------------------------
    if len(arr) != n:
        print("\nErro: a quantidade de números digitados não corresponde ao valor de n.")
        print(f"n informado: {n}")
        print(f"Quantidade digitada: {len(arr)}")
        return

# ------------------------------
# Algoritmo principal
# ------------------------------
    moves = 0
    previous = arr[0]

    for value in arr[1:]:
        if value < previous:
            moves += previous - value
        else:
            previous = value

    print("Número mínimo de incrementos:", moves)



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
