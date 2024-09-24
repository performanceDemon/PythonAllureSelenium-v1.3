# Algoritmos de ordenación, búsqueda y manejo de estructuras de datos

listaparaValidad = [34,344,435,1,4,6,89,89,56]
# Quicksort
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Búsqueda en profundidad (DFS) en un grafo representado como un diccionario
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")
    for next_node in graph[start] - visited:
        dfs(graph, next_node, visited)

# Búsqueda en amplitud (BFS) en un grafo
from collections import deque
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            queue.extend(graph[node] - visited)

# Manipulación de cadenas

# Revertir una cadena
def reverse_string(s):
    return s[::-1]

# Verificar si una cadena es un palíndromo
def is_palindrome(s):
    return s == s[::-1]

# Resolución de problemas matemáticos

# Factorial de un número
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Generar la serie de Fibonacci
def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
    return fib_sequence[:n]

def invertir_lista(lista):
    return lista[::-1]

# Ejemplo de uso:
numeros = [1, 2, 3, 4, 5]
resultado = invertir_lista(numeros)
print(resultado)  # Salida: [5, 4, 3, 2, 1]

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

arr = [3, 6, 8, 10, 1, 2, 1,54,67,34,23,87]
print(quicksort(arr))

def is_palindrome(s):
    s = ''.join(e for e in s if e.isalnum()).lower()
    return s == s[::-1]

print(is_palindrome("A man, a plan, a canal: Panama"))  # True



lista2 = invertir_lista(resultado)
print(lista2)
def alcuadrado(lista):
    return list(map(lambda x: x**2, lista))

# Ejemplo de uso:
numeros = [1, 2, 3, 4, 5]
resultado = alcuadrado(numeros)
print(resultado)  # Salida: [1, 4, 9, 16, 25]


# Ordenamiento de burbuja
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Uso de pytest y doctest para la función de suma de una lista


print(bubble_sort(listaparaValidad))
