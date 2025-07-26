"""
- Añadir
- Ver
- Buscar
- Eliminar
"""


def add_contact(name, phone):
    global contacts
    contact = {"name": name, "phone": phone}
    print(f"Contacto {name} añadido.\n")
    contacts.append(contact)


def view_contacts():
    if not contacts:
        print("No hay contactos para mostrar.")
    else:
        for contact in contacts:
            print(
                f"Nombre: {contact.get("name", "")},",
                f" Teléfono: {contact.get("phone", "")}",
            )


def search_contact(name=""):
    contact_search = None
    for contact in contacts:
        if contact.get("name", "") == name:
            contact_search = contact
    if contact_search:
        print(
            f"Nombre: {contact_search.get('name', '')},",
            f" Teléfono: {contact_search.get('phone', '')}",
        )
    else:
        print(f"No se encontró el contacto con el nombre: {name}")


def delete_contact(name):
    global contacts
    index = [i for i, contact in enumerate(contacts)
             if contact.get("name", "") == name]
    if not index:
        raise ValueError("No se encotro el elemento a eliminar")
    contact_remove = contacts.pop(index[0])
    print(f"Contacto {contact_remove['name']} eliminado.", end="\n")


def display_menu():
    print("Gestor de Contactos")
    print("1. Añadir")
    print("2. Ver")
    print("3. Buscar")
    print("4. Eliminar")
    print("5. Salir", end="\n")


def select_option():
    try:
        choice = input("Seleccione una opción (1-5): ")
        print()

        while choice != "5":
            if choice == "1":
                name = input("Ingrese el nombre del contacto: ")
                phone = input("Ingrese el número de teléfono del contacto: ")
                add_contact(name, phone)
            elif choice == "2":
                view_contacts()
                print()
            elif choice == "3":
                name = input("Ingrese el nombre del contacto: ")
                search_contact(name)
                print()
            elif choice == "4":
                name = input("Ingrese el nombre del contacto: ")
                delete_contact(name)
            else:
                print("Opción no válida. Vuelva a intentarlo.")
            display_menu()
            choice = input("Seleccione una opción (1-5): ")
            print()
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        print("Saliendo del programa...")


def main():
    display_menu()
    select_option()


contacts = []


if __name__ == "__main__":
    main()
