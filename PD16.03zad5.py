# Napisać funkcję, która konwertuje liczbę z systemu dziesiętnego na binarny
# (nie używamy funkcji wbudowanych w Pythonie)

def bi_convert(number: int) -> int:
    result = ""
    while number > 0:
        result = str(number % 2) + result
        number = number // 2

    return result

print(bi_convert(5))