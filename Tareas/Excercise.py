def sum(list):
    result = 0
    error = []
    try:
        for item in list:
            if not isinstance(item, (int, float)):
                error.append(item)
                raise TypeError("El item: {item} debe ser de tipo "
                                "int or float.")
            result += item
    except TypeError:
        print("Error: All items in the list must be numbers.")
    return result, error


sum_result = sum([1, 2, 3, 4, 5])
print(f"The sum of the list is: {sum_result[0]}, with errors: {sum_result[1]}")

sum_result = sum([1, "two", 3])
print(f"The sum of the list is: {sum_result[0]}, with errors: {sum_result[1]}")
