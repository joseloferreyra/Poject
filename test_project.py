import pytest
import os
import csv
from project import GestorLibros  # Asegúrate de que el nombre del archivo sea project.py

@pytest.fixture
def setup_csv():
    # Crear un archivo CSV temporal para las pruebas
    test_file = 'test_library.csv'
    gestor = GestorLibros(test_file)

    # Escribir algunos libros de prueba
    with open(test_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Libro 1', 'Autor 1', 'Género 1', '2023'])
        writer.writerow(['Libro 2', 'Autor 2', 'Género 2', '2022'])

    yield gestor, test_file

    # Eliminar el archivo temporal después de las pruebas
    os.remove(test_file)

def test_agregar_libro(setup_csv):
    gestor, test_file = setup_csv
    gestor.agregar_libro(['Libro 3', 'Autor 3', 'Género 3', '2021'])

    with open(test_file, 'r') as file:
        reader = csv.reader(file)
        libros = list(reader)

    assert ['Libro 3', 'Autor 3', 'Género 3', '2021'] in libros

def test_mostrar_libros(setup_csv):
    gestor, _ = setup_csv
    libros = gestor.mostrar_libros()
    assert len(libros) == 2
    assert libros[0] == ['Libro 1', 'Autor 1', 'Género 1', '2023']

def test_borrar_libro(setup_csv):
    gestor, test_file = setup_csv
    result = gestor.borrar_libro(['Libro 1', 'Autor 1', 'Género 1', '2023'])

    assert result is True

    with open(test_file, 'r') as file:
        reader = csv.reader(file)
        libros = list(reader)

    assert ['Libro 1', 'Autor 1', 'Género 1', '2023'] not in libros
    assert ['Libro 2', 'Autor 2', 'Género 2', '2022'] in libros

def test_editar_libro(setup_csv):
    gestor, test_file = setup_csv
    gestor.editar_libro(['Libro 1', 'Autor 1', 'Género 1', '2023'], ['Libro Editado', 'Autor Editado', 'Género Editado', '2024'])

    with open(test_file, 'r') as file:
        reader = csv.reader(file)
        libros = list(reader)

    assert ['Libro Editado', 'Autor Editado', 'Género Editado', '2024'] in libros
    assert ['Libro 1', 'Autor 1', 'Género 1', '2023'] not in libros

if __name__ == "__main__":
    pytest.main()