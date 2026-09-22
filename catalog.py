

from validations import (
    validate_description,
    validate_not_empty,
    validate_price,
    validate_status,
)


def add_piece(catalog, piece_id, name, category, price, status, description):

    validate_not_empty(piece_id, "id")
    validate_not_empty(name, "name")
    validate_not_empty(category, "category")

    validated_price = validate_price(price)
    validated_status = validate_status(status)
    validated_description = validate_description(description)

    new_piece = {
        "id": str(piece_id).strip(),
        "name": str(name).strip(),
        "category": str(category).strip(),
        "price": validated_price,
        "status": validated_status,
        "description": validated_description.strip(),
    }

    catalog.append(new_piece)
    return new_piece


def list_pieces(catalog):

    if not isinstance(catalog, list):
        raise ValueError("Error: The catalog must be a valid list.")

    if not catalog:
        return []

    return [piece["name"] for piece in catalog]


def find_piece_by_id(catalog, piece_id):

    if not isinstance(catalog, list):
        raise ValueError("Error: The catalog must be a valid list.")

    if not piece_id or not str(piece_id).strip():
        raise ValueError("Error: The piece ID cannot be empty.")

    target_id = str(piece_id).strip()

    for piece in catalog:
        if piece["id"] == target_id:
            return piece

    return None


def delete_piece(catalog, piece_id):

    if not isinstance(catalog, list):
        raise ValueError("Error: The catalog must be a valid list.")

    if not piece_id or not str(piece_id).strip():
        raise ValueError("Error: The piece ID cannot be empty.")

    target_id = str(piece_id).strip()

    for index, piece in enumerate(catalog):
        if piece["id"] == target_id:
            return catalog.pop(index)

    return None