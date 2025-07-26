product = {
    "name": "Laptop",
    "price": 999.99,
    "stock": 10,
    "category": "Electronics"
    }

# Agregar un nuevo campo "discount" al diccionario
product["discount"] = 0.1

# Actualizar el valor del campo "stock"
product["stock"] = 15

del product["category"]
# product.pop("price", "Not Found")

set_1 = {1, 2, 3, 4, 5}
set_2 = set(range(6, 11))

# Unir los dos conjuntos
set_union_1 = set_1 & set_2
set_union_2 = set_1.union(set_2)

# Intersección de los dos conjuntos
set_intersection_1 = set_1 | set_2
set_intersection_2 = set_1.intersection(set_2)
