
import pytest
from data_validator.validator import is_valid_name

@pytest.mark.parametrize("name, expected", [
    ("Juan", True),               # Nombre simple válido
    ("Ana María", True),         # Nombre compuesto con espacio
    ("A", False),                # Muy corto
    ("Juan123", False),         # Contiene números
    ("", False),                # Vacío
    ("María-José", False),      # Contiene guión (no permitido en esta versión)
    ("José!", False),           # Contiene símbolo
    ("Carlos Alberto", True),   # Otro nombre compuesto válido
])
def test_is_valid_name(name, expected):
    assert is_valid_name(name) == expected