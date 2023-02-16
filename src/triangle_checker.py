def is_triangle(a: int, b: int, c: int) -> bool:
    """Recebe 3 valores e retorna se é possível formar um triangulo."""
    return a + b > c and a + c > b and b + c > a


def triangle_checker(a: int, b: int, c: int) -> str:
    """Recebe 3 valores e informa qual tipo de triangulo é possível formar."""
    if not is_triangle(a, b, c):
        return "não é triângulo"
    elif a == b == c:
        return "Triângulo Equilátero: três lados iguais"
    elif a != b != c:
        return "Triângulo Escaleno: três lados diferentes."
    else:
        return "Triângulo Isósceles: quaisquer dois lados iguais;"


print(triangle_checker(5, 3, 7))
print(triangle_checker(5, 5, 5))
print(triangle_checker(5, 5, 7))
print(triangle_checker(5, 50, 2))
