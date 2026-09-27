

ALLOWED_STATUSES = {"disponible", "reservada", "vendida"}


def validate_not_empty(value, field_name):

    if not value or not str(value).strip():
        raise ValueError(f"Error: The field '{field_name}' cannot be empty.")


def validate_price(price):

    try:
        numeric_price = float(price)
    except (ValueError, TypeError):
        raise ValueError("Error: The price must be a valid numeric value.")

    if numeric_price <= 0:
        raise ValueError("Error: The price must be greater than zero.")
    return numeric_price


def validate_status(status):

    if not status or status.strip().lower() not in ALLOWED_STATUSES:
        raise ValueError(f"Error: Invalid status. Allowed statuses are: {', '.join(ALLOWED_STATUSES)}")
    return status.strip().lower()


def validate_description(description):

    if not description:
        raise ValueError("Error: Description cannot be empty.")

    desc_lower = description.lower()
    if "usada" not in desc_lower and "certificada" not in desc_lower:
        raise ValueError("Error: The description must include either 'usada' or 'certificada'.")
    return description

