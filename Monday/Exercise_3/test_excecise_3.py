from main import calculateArea


def test_calculateArea(capsys, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "5")
    calculateArea()
    response = capsys.readouterr()
    assert response.out == "Resultado: El área del circulo es 78.54\n"
