import pytest
from catalog import (
    add_piece,
    list_pieces,
    find_piece_by_id,
    remove_piece,
    get_average_price
)


@pytest.fixture
def sample_catalog():
    """Fixture que proporciona un catálogo limpio con algunos vinilos de prueba."""
    catalog = []
    add_piece(catalog, "V01", "Abbey Road", "Rock", 25.50, "nuevo", "Edición usada remasterizada")
    add_piece(catalog, "V02", "Kind of Blue", "Jazz", 30.00, "usado", "Versión certificada original")
    return catalog


def test_add_piece_success(sample_catalog):
    """Verifica que se pueden añadir piezas correctamente y limpia los espacios."""
    add_piece(sample_catalog, "  V03  ", " Thriller ", "Pop", 20.0, "como nuevo", "Edición usada especial")
    assert len(sample_catalog) == 3
    assert sample_catalog[2]["id"] == "V03"
    assert sample_catalog[2]["name"] == "Thriller"


def test_add_duplicate_id(sample_catalog):
    """Verifica que no se permite añadir un vinilo con un ID duplicado."""
    with pytest.raises(ValueError):
        add_piece(sample_catalog, "V01", "Duplicate Album", "Rock", 15.0, "nuevo", "Edición usada")


def test_find_piece_existing(sample_catalog):
    """Verifica que se encuentra una pieza existente por su ID."""
    piece = find_piece_by_id(sample_catalog, "V01")
    assert piece is not None
    assert piece["name"] == "Abbey Road"


def test_find_piece_non_existing(sample_catalog):
    """Verifica que devuelve None si el ID no existe en el catálogo."""
    piece = find_piece_by_id(sample_catalog, "V99")
    assert piece is None


def test_remove_piece_success(sample_catalog):
    """Verifica que se puede eliminar una pieza existente y devuelve True."""
    result = remove_piece(sample_catalog, "V01")
    assert result is True
    assert len(sample_catalog) == 1


def test_remove_piece_non_existing(sample_catalog):
    """Verifica que intentar eliminar un ID inexistente devuelve False."""
    result = remove_piece(sample_catalog, "V99")
    assert result is False
    assert len(sample_catalog) == 2


def test_get_average_price(sample_catalog):
    """Verifica el cálculo correcto del precio promedio del catálogo."""
    avg = get_average_price(sample_catalog)
    # (25.50 + 30.00) / 2 = 27.75
    assert avg == 27.75


def test_get_average_price_empty():
    """Verifica el comportamiento al calcular el precio medio con un catálogo vacío."""
    empty_catalog = []
    assert get_average_price(empty_catalog) == 0.0