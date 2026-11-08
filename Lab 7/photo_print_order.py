import math


def parse_order(text):
    """Parse a print order in the format SIZE:COPIES."""
    if not isinstance(text, str):
        return "", 0

    parts = text.split(":")
    if len(parts) != 2:
        return "", 0

    size, copies_text = parts
    size = size.strip()

    if not size:
        return "", 0

    try:
        copies = int(copies_text.strip())
    except (ValueError, TypeError):
        return "", 0

    if copies < 0:
        return "", 0

    return size.upper(), copies


def file_size_average(sizes_csv):
    """Return the integer average of comma-separated file sizes."""
    if not isinstance(sizes_csv, str) or not sizes_csv.strip():
        return 0

    try:
        values = [int(value.strip()) for value in sizes_csv.split(",")]
    except (ValueError, TypeError):
        return 0

    if not values or any(value < 0 for value in values):
        return 0

    return sum(values) // len(values)


def payable_amount(text):
    """Calculate the payable amount from AMOUNT|DISCOUNT."""
    if not isinstance(text, str):
        return 0.0

    parts = text.split("|")
    if len(parts) != 2:
        return 0.0

    try:
        amount = float(parts[0].strip())
        discount = float(parts[1].strip())
    except (ValueError, TypeError):
        return 0.0

    if not math.isfinite(amount) or not math.isfinite(discount):
        return 0.0

    if amount < 0 or discount < 0:
        return 0.0

    total = amount * 1.18 - discount
    return max(total, 0.0)


def main():
    print("==== Running parse_order ====")
    user_input = input("Enter print size:copies (e.g. 4x6:25): ")
    result = parse_order(user_input)
    print("Size and Copies:", result)

    print("\n==== Running file_size_average ====")
    user_input = input("Enter file sizes in MB as CSV (e.g. 4,8,12): ")
    result = file_size_average(user_input)
    print("Average File Size:", result)

    print("\n==== Running payable_amount ====")
    user_input = input("Enter amount|discount (e.g. 450|50): ")
    result = payable_amount(user_input)
    print("Payable Amount:", result)


if __name__ == "__main__":
    main()
