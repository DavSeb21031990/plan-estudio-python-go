books = []
# Agregar elementos a la lista
books.append("Alexander")
books.append("2012")
books.append("Naruto Shippuden - The Lost Tower")
books.append("Naruto Shippuden - The Last")

# Insertar un elemento en una posición específica
books.insert(1, "1408")

# Eliminar un elemento de una posición específica
books.pop(2)
books.append("2012")
books.append("Gastby")
print(books)

# Eliminar un elemento
books.remove("Gastby")

print(books)

# Ordenar
books.sort()
print(books)

# Invertir el orden de los elementos
books_copy_1 = books[:]
books_copy_1.reverse()
print(books_copy_1)

books_copy_2 = books[:]
books_copy_2.sort(reverse=True)
print(books_copy_2)

books_copy = books[::-1]
print(books_copy)
