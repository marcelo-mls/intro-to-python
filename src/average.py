def find_average_with_for(numbers: list[int]) -> float:
    """Calcula a média aritmética dos valores contidos em uma lista"""
    total = 0
    for number in numbers:
        total += number

    return total / len(numbers)


def find_average(numbers: list[int]) -> float:
    """Calcula a média aritmética dos valores contidos em uma lista"""
    return sum(numbers) / len(numbers)


print(find_average_with_for([4, 20]))
print(find_average_with_for([40, 2, 5, 5]))
print(find_average([4, 20]))
print(find_average([40, 2, 5, 5]))
