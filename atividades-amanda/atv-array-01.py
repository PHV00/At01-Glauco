"""
-------------------------------------------------------------------------------------------------------------------------------------
Disciplina: Algoritmos Avançados   
Curso: Engenharia de Software  
Aluno(a): Amanda Korczagin
Professor: Glauco Scheffel
-------------------------------------------------------------------------------------------------------------------------------------

Problema: Distinct Numbers (CSES)

-> Complexidade: 
Tempo: 1s
Memória: 512MB

-> Estrutura principal utilizada: 
Array, nível fácil 

-> Fonte do exercício:
https://cses.fi/problemset/task/1621/

-> Descrição do problema: 
Dado um array de n números inteiros, determine quantos valores distintos existem no array

-> Estratégia V1 (Feita por mim):
Ordenar o array e percorrer comparando elementos consecutivos.
Sempre que o valor atual for diferente do anterior, incrementamos o contador. 
Essa estratégia evita o uso de estruturas auxiliares, mas exige ordenação. 

Entrada: 
A primeira linha contém um número inteiro n: o tamanho do array.
A segunda linha contém n inteiros, x1, x2, etc.

Saída:
Impressão de um único número inteiro, a quantidade de valores distintos.

Restrições:
1 <= n <= 2 x 10^5
1 <= x_i <= 10^9

Exemplo

Entrada:
6
3 6 4 7 6 6 

Saída
4

-> Justificativa da estrutura
O array é adequado por o problema exige apenas acesso sequencial e comparação entre os elementos.

"""

# V1 - Feito por mim
def solve_v1():

    print("Digite o valor de n para a quantidade de números inteiros no array: ")

    try:
        n = int(input())
    except ValueError:
        print("Erro: n deve ser um número inteiro")
        return
    
    print("Digite os {n} números separados por espaço: ")

    arr = list(map(int, input().split()))

    #Validação da quantidade digitada
    if len(arr) != n:
        print("Erro: quantidade de números indicados diferente de n.")
        return
    
    arr.sort()

    contador = 1

    for i in range(1,n):
        if arr[i] != arr[i-1]:
            contador += 1

    print("Quantidade de valores ditintos: ", contador)

"""
Seleção do uso de IA nesta atividade

-> Prompt utilizado:
"Estou desenvolvendo a atividade Distinct Numbers do CSES, minha ideia é ordenar o array e contar quantas vezes o valor muda em relação ao termo anterior.
O que você acha da minha ideia? Pode sugerir uma versão melhor?"

-> O que foi aproveitado:
Validei minha estratégia baseada na ordenação dos termos e entendi as sugestões de organização estrutural do código.

-> O que foi adaptado:
Mantive a lógica principal desenvolvida, estruturei melhor as validações na entrada e ajustei a organização do código para maior clareza. 

-> Reflexão final:
A IA foi utilizada como ferramenta de validação estratégica e melhoria estrutural do código.

"""

# V2 - feito por IA
def solve_v2():
    print("Digite o valor de n e pressione Enter: ")

    try:
        n = int(input())
    except ValueError:
        print("Erro: n deve ser um número inteiro.")
        return
    
    if n == 0:
        print("Quantidade de valores distintos: 0")
        return
    
    print("Digite os {n} números separados por espaço e pressione Enter: ")

    arr = []
    while len(arr) < n:
        try:
            arr.extend(map(int, input().split()))
        except ValueError:
            print("Erro: todos os valores devem ser inteiros.")
            return
    
    if len(arr) != n:
        print("Erro: quantidade incorreta de valores")
        return
    
    #Utiliza set para eliminar duplicatas
    distintos = len(set(arr))

    print("Quantidade de valores distintos: ", distintos)

# Menu principal

if __name__ == "__main__":

    print("Digite 1 para executar a V1 (minha versão): ")
    print("Digite 2 para executar a V2 (feita pela IA)")

    opcao = input ("Escolha a opção: ")

    if opcao == "1":
        solve_v1()
    elif opcao == "2":
        solve_v2()
    else:
        print("Opção inválida.")


