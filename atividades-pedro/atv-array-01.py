"""
-------------------------------------------------------------------------------------------------------------------------------------
Disciplina: Algoritmos Avançados   
Curso: Engenharia de Software  
Aluno(a): Pedro Henrique Vitoreti
Professor: Glauco Scheffel
-------------------------------------------------------------------------------------------------------------------------------------
Nome do problema : Union of Arrays with Duplicates
Link do problema : https://www.geeksforgeeks.org/problems/union-of-two-arrays3538/1
Plataforma utilizada : GeeksforGeeks 
Estrutura de dados principal usada :  para o meu codigo Array dinâmico e para o gerado por ia Hash Set
Justificativa: Pois enquanto o array dinâmico é uma estrutura de dados que pode armazenar elementos 
de forma contígua e permite acesso rápido por índice, oque me permitiu preliminarmente resolver o problema, 
o hash set é uma estrutura de dados que armazena elementos únicos e oferece operações eficientes de inserção,
busca e união, oque me permitiu transformar a função em algo mais legivel e simples.
-------------------------------------------------------------------------------------------------------------------------------------
"""

"""
PROBLEMA:

Dado dois arrays, a[] e b[], retorne a união de ambos os arrays em qualquer ordem.
A união de dois arrays é uma coleção de todos os elementos distintos presentes em qualquer um dos arrays. Se um elemento aparecer mais de uma vez em um ou em ambos os arrays, ele deverá ser incluído apenas uma vez no resultado.

Observação: Os elementos de a[] e b[] não são necessariamente distintos.
Observe também que você pode retornar a união em qualquer ordem, mas o código principal imprimirá o resultado apenas em ordem crescente.

Exemplos:

Input: a[] = [1, 2, 3, 2, 1], b[] = [3, 2, 2, 3, 3, 2]
Output: [1, 2, 3]
Explicação: O conjunto união de ambas as matrizes será 1, 2 e 3.

Input: a[] = [1, 2, 3], b[] = [4, 5, 6] 
Output: [1, 2, 3, 4, 5, 6]
Explicação: O conjunto união de ambas as matrizes será 1, 2, 3, 4, 5 e 6.

Input: a[] = [1, 2, 1, 1, 2], b[] = [2, 2, 1, 2, 1] 
Output: [1, 2]
Explicação: A união dos dois arrays resultará em 1 e 2.

Restrições:

1 ≤ a.size(), b.size() ≤ 106
0 ≤ a[i], b[i] ≤ 105

"""

# V1 - Feita por mim
a = [1, 2, 3, 2, 1]
b = [3, 2, 2, 3, 3, 2]

def unionFunction(a, b):
    union = []
    for item in a:
        if item not in union:
            union.append(item)
    for item in b:
        if item not in union:
            union.append(item)
    return sorted(union)

print("Por mim"+str(unionFunction(a, b)))

# V2 - Feita com ia
a = [1, 2, 3, 2, 1]
b = [3, 2, 2, 3, 3, 2]

def unionFunction(a, b):
    union = set(a) | set(b)
    return list(union)

print("Pela IA"+str(unionFunction(a, b)))