import pytest
from validations import validate_not_empty, validate_price, validate_status, validate_description


# --- Pruebas para validate_not_empty ---
@pytest.mark.parametrize("input_value", [
    "Rock",
    "Jazz y Blues",
    "Electrónica"
])
def test_validate_not_empty_valid(input_value):
    assert validate_not_empty(input_value) == input_value.strip()


@pytest.mark.parametrize("invalid_value", [
    "",
    "   ",
    None,
    123,
    True
])
def test_validate_not_empty_invalid(invalid_value):
    with pytest.raises((ValueError, TypeError)):
        validate_not_empty(invalid_value)


# --- Pruebas para validate_price ---
@pytest.mark.parametrize("valid_price_input, expected_output", [
    ("15.50", 15.50),
    (20, 20.0),
    ("  30  ", 30.0)
])
def test_validate_price_valid(valid_price_input, expected_output):
    assert validate_price(valid_price_input) == expected_output


@pytest.mark.parametrize("invalid_price_input", [
    "-5",
    "0",
    "abc",
    "",
    None,
    True,
    False
])
def test_validate_price_invalid(invalid_price_input):
    with pytest.raises((ValueError, TypeError)):
        validate_price(invalid_price_input)


# --- Pruebas para validate_status ---
@pytest.mark.parametrize("valid_status, expected_output", [
    ("NUEVO", "nuevo"),
    ("  Usado  ", "usado"),
    ("como nuevo", "como nuevo")
])
def test_validate_status_valid(valid_status, expected_output):
    assert validate_status(valid_status) == expected_output


@pytest.mark.parametrize("invalid_status", [
    "",
    "   ",
    None,
    123
])
def test_validate_status_invalid(invalid_status):
    with pytest.raises((ValueError, TypeError)):
        validate_status(invalid_status)


# --- Pruebas para validate_description ---
@pytest.mark.parametrize("valid_desc", [
    "Edición usada de coleccionista",
    "Versión certificada y firmada",
    "usada en perfecto estado"
])
def test_validate_description_valid(valid_desc):
    assert validate_description(valid_desc) == valid_desc.strip()


@pytest.mark.parametrize("invalid_desc", [
    "Disco normal sin sello",
    "",
    None,
    123
])
def test_validate_description_invalid(invalid_desc):
    with pytest.raises((ValueError, TypeError)):
        validate_description(invalid_desc)