import pytest
from main import calculateArea
from unittest.mock import patch


def test_calculateArea(capsys):
    with patch("builtins.input", return_value="5"):
        calculateArea()
        response = capsys.readouterr()
        assert response.out == "Resultado: El área del circulo es 78.54\n"
