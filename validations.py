ALLOWED_STATUSES = {"disponible", "reservada", "vendida", "nuevo", "usado", "como nuevo"}


def validate_not_empty(value, field_name="campo"):
    if not value or not str(value).strip():
        raise ValueError(f"Error: The field '{field_name}' cannot be empty.")
    if not isinstance(value, str):
        raise TypeError("Error: The value must be a string.")
    return str(value).strip()


def validate_price(price):
    if isinstance(price, bool):
        raise TypeError("Error: The price cannot be a boolean.")
    try:
        numeric_price = float(price)
    except (ValueError, TypeError):
        raise ValueError("Error: The price must be a valid numeric value.")

    if numeric_price <= 0:
        raise ValueError("Error: The price must be greater than zero.")
    return numeric_price


def validate_status(status):
    if not isinstance(status, str):
        raise TypeError("Error: Status must be a string.")
    cleaned_status = status.strip().lower()
    if cleaned_status not in ALLOWED_STATUSES:
        raise ValueError(f"Error: Invalid status. Allowed statuses are: {', '.join(ALLOWED_STATUSES)}")
    return cleaned_status


def validate_description(description):
    if not isinstance(description, str):
        raise TypeError("Error: Description must be a string.")
    if not description.strip():
        raise ValueError("Error: Description cannot be empty.")

    desc_lower = description.lower()
    if "usada" not in desc_lower and "certificada" not in desc_lower:
        raise ValueError("Error: The description must include either 'usada' or 'certificada'.")
    return description