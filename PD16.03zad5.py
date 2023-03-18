# Napisać funkcję, która konwertuje liczbę z systemu dziesiętnego na binarny
# (nie używamy funkcji wbudowanych w Pythonie)

def bi_convert(number: int) -> int:
    result = ""
    while number > 0:
        result = str(number % 2) + result
        number = number // 2

    return result

print(bi_convert(10))

def dec_to_bin(value: int) -> list:
    parts = []
    while value != 0:
        parts.append(value % 2)
        # dzielone przez 2 bez reszty
        value //= 2
    # swpak
    return parts[::-1]

print(dec_to_bin(10))