

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