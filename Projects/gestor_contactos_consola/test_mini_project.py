import pytest
import mini_project


@pytest.fixture
def clean_contacts():
    """Fixture to reset contacts before each test."""
    mini_project.contacts = []
    yield


def test_add_contact(clean_contacts):
    mini_project.add_contact("Alice", "123456789")
    assert len(mini_project.contacts) == 1
    assert mini_project.contacts[0]["name"] == "Alice"
    assert mini_project.contacts[0]["phone"] == "123456789"


def test_view_contacts(capsys):
    mini_project.contacts = [{"name": "Alice", "phone": "123456789"}]
    mini_project.view_contacts()
    captured = capsys.readouterr()
    assert "Nombre: Alice,  Teléfono: 123456789" in captured.out


def test_search_contact_found(capsys):
    mini_project.contacts = [{"name": "Alice", "phone": "123456789"}]
    mini_project.search_contact("Alice")
    captured = capsys.readouterr()
    assert "Nombre: Alice,  Teléfono: 123456789" in captured.out


def test_search_contact_not_found(capsys):
    mini_project.contacts = [{"name": "Alice", "phone": "123456789"}]
    mini_project.search_contact("Bob")
    captured = capsys.readouterr()
    assert "No se encontró el contacto con el nombre: Bob" in captured.out
