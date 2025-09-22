
import pytest
from data_validator.validator import is_valid_dni

@pytest.mark.parametrize("dni, expected", [
    ("1234567", True),      # 7 dígitos válidos
    ("12345678", True),     # 8 dígitos válidos
    ("123456", False),      # Menos de 7 dígitos
    ("123456789", False),   # Más de 8 dígitos
    ("12A45678", False),    # Contiene letras
    ("", False),            # Vacío
    ("00000000", True),     # Caso límite válido
])
def test_is_valid_dni(dni, expected):
    assert is_valid_dni(dni) == expected