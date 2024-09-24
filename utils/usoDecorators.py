import pytest

def debug_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Running {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@debug_decorator
def nombreAgregarFuncion(a, b):
    return a + b

listaint = [34,3,34,43,5]
def sum_list(listaint):
    return print(sum(listaint))

def test_sum_list():
    assert sum_list([1, 2, 3]) == 6
    assert sum_list([0, 0, 0]) == 0
    assert sum_list([-1, 1, 0]) == 0

# Prueba de la función
if __name__ == "__main__":
    result = nombreAgregarFuncion(3, 4)  # Esto debería imprimir detalles del decorador
    print(f"Resultado final: {result}")