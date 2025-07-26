def resolve(*numbers, **operations):
    for key, value in operations.items():
        for operation in value:
            if operation == "add":
                result = sum(numbers)
                print(f"Suma: {result:.2f}")
            elif operation == "subtract":
                result = substract(numbers)
                print(f"Resta: {result:.2f}")
            elif operation == "multiply":
                result = multiply(numbers)
                print(f"Multiplicación: {result:.2f}")
            elif operation == "divide":
                result = divide(numbers)
                print(f"División: {result:.2f}")
            else:
                print(f"Operación '{operation}' no reconocida.")


def sum(*numbers):
    result = 0
    for number in numbers:
        result += number
    return result


def substract(*numbers):
    result = numbers[0]
    for number in numbers[1:]:
        result -= number
    return result


def multiply(*numbers):
    result = 1
    for number in numbers:
        result *= number
    return result


def divide(*numbers):
    if 0 in numbers:
        print("Error: División por cero.")
        return 0
    result = numbers[0]
    for number in numbers[1:]:
        result /= number
    return result


resolve(1, 2, 3, operations=("add", "subtract", "multiply"))
print("Programa finalizado.")
