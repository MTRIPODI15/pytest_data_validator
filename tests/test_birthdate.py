
import pytest
from data_validator.validator import is_valid_birthdate
from datetime import datetime, timedelta

@pytest.mark.parametrize("date_str, expected", [
    ("1990-05-20", True),                         # Fecha válida en el pasado
    ("2020-01-01", True),                         # Fecha reciente pero válida
    ("2030-12-31", False),                        # Fecha en el futuro
    ("2000-02-30", False),                        # Fecha inválida (febrero 30 no existe)
    ("abcd-ef-gh", False),                        # Formato inválido
    ("", False),                                  # Vacío
    (datetime.now().strftime("%Y-%m-%d"), False), # Fecha de hoy (no es anterior)
    ((datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d"), True), # Ayer
])
def test_is_valid_birthdate(date_str, expected):
    assert is_valid_birthdate(date_str) == expected