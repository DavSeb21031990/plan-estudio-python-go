import pytest
from week2_python_poo.mi_paquete.calculadora import sumar, restar

@pytest.mark.parametrize("a, b, expected", [
    (2, 2, 4),
    (1, 1, 2)
])
def test_suma(a, b, expected):
    assert sumar(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (2, 2, 0),
    (1, 1, 0)
])
def test_resta(a, b, expected):
    assert restar(a, b) == expected