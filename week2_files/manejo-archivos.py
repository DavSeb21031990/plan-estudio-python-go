from pathlib import Path
import csv


def write_lines_to_file():
    new_lines = []
    if option == 'si':
        while True:
            try:
                new_line = input('Ingrese una linea: ')
                if not new_line.endswith('.'):
                    new_lines.append(new_line)
                else:
                    return new_lines
            except EOFError:
                return new_lines
    return new_lines


def create_file(name_file, new_lines):
    try:
        with open(name_file, 'w') as file:
            if new_lines:
                for new_line in new_lines:
                    add_line(name_file, new_line)
    except PermissionError:
        print("No tiene permisos para crear el archivo.")
    except Exception as e:
        print("Ocurrio un error al crear el archivo:", e)


def add_line(name_file, new_line):
    if not new_line:
        return
    with open(name_file, 'a') as file:
        file.write(new_line + "\n")


def read_file(name_file):
    try:
        with open(name_file, 'r') as file:
            for read_line in file:
                print(read_line.strip())
    except FileNotFoundError:
        print("El archivo no existe.")
    except Exception as e:
        print("Ocurrio un error al leer el archivo:", e)


def create_file_csv(name_file):
    with open(name_file, 'w', newline='', encoding='UTF-8') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow([1, 'Java'])
        writer.writerow([2, 'Python'])

def load_csv(name_file):
    with open(name_file, 'r', newline='', encoding='UTF-8') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            print(row)

if __name__ == "__main__":
    option = input('Quiere ingresar texto al archivo?')
    lines = write_lines_to_file()
    create_file("archivo.txt", lines)
    read_file("archivo.txt")

    # Archivo Csv
    create_file_csv("archivo.csv")
    load_csv("archivo.csv")