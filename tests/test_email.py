
import pytest
from data_validator.validator import is_valid_email

#Creo varios casos verificando el comportamiento del programa

@pytest.mark.parametrize("email, expected", [
    ("user@example.com", True),
    ("user.name@domain.co", True),
    ("user@sub.domain.com", True),
    ("invalid-email", False),
    ("user@.com", False),
    ("@domain.com", False),
    ("user@domain", False),
])
def test_is_valid_email(email, expected):
    assert is_valid_email(email) == expected