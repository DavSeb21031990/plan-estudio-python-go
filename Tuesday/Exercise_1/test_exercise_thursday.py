from exercise_thursday import validate_is_pair, get_number


def test_validate_is_pair(capsys):
    validate_is_pair(2)
    captured = capsys.readouterr()
    assert captured.out == "El número es par\n"


def test_get_number(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "5")
    assert get_number() == 5
