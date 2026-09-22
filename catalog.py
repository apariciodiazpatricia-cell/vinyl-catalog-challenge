

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


def remove_piece(catalog, piece_id):

    if not isinstance(catalog, list):
        raise ValueError("Error: The catalog must be a valid list.")

    if not piece_id or not str(piece_id).strip():
        raise ValueError("Error: The piece ID cannot be empty.")

    target_id = str(piece_id).strip()

    try:
        found_index = -1
        for index, piece in enumerate(catalog):
            if piece["id"] == target_id:
                found_index = index
                break

        if found_index == -1:
            raise ValueError(f"Error: Piece with ID '{target_id}' was not found.")

        catalog.pop(found_index)
        return True

    except ValueError as e:

        return False


def update_piece(catalog, piece_id, price=None, status=None, description=None):

    if not isinstance(catalog, list):
        raise ValueError("Error: The catalog must be a valid list.")

    if not piece_id or not str(piece_id).strip():
        raise ValueError("Error: The piece ID cannot be empty.")

    target_id = str(piece_id).strip()

    piece = None
    for item in catalog:
        if item["id"] == target_id:
            piece = item
            break

    if not piece:
        return None

    if price is not None:
        piece["price"] = validate_price(price)

    if status is not None:
        piece["status"] = validate_status(status)

    if description is not None:
        validated_desc = validate_description(description)
        piece["description"] = validated_desc.strip()

    return piece


def get_catalog_summary(catalog):

    if not isinstance(catalog, list):
        raise ValueError("Error: The catalog must be a valid list.")

    summary = {}
    for piece in catalog:
        category = piece.get("category")
        if category:
            summary[category] = summary.get(category, 0) + 1

    return summary


def get_pieces_by_category(catalog, category):

    if not isinstance(catalog, list):
        raise ValueError("Error: The catalog must be a valid list.")

    matching_names = []
    for piece in catalog:
        if piece.get("category") == category:
            matching_names.append(piece.get("name"))

    return matching_names


def piece_exists(catalog, piece_id):

    if not isinstance(catalog, list):
        raise ValueError("Error: The catalog must be a valid list.")

    if not piece_id or not str(piece_id).strip():
        return False

    target_id = str(piece_id).strip()

    for piece in catalog:
        if piece.get("id") == target_id:
            return True

    return False


def filter_by_status(catalog, status):

    if not isinstance(catalog, list):
        raise ValueError("Error: The catalog must be a valid list.")


    validated_status = validate_status(status)

    matching_pieces = []
    for piece in catalog:
        if piece.get("status") == validated_status:
            matching_pieces.append(piece)

    return matching_pieces


def filter_by_min_price(catalog, min_price):

    if not isinstance(catalog, list):
        raise ValueError("Error: The catalog must be a valid list.")


    validated_min_price = validate_price(min_price)

    matching_pieces = []
    for piece in catalog:
        if piece.get("price", 0) > validated_min_price:
            matching_pieces.append(piece)

    return matching_pieces
