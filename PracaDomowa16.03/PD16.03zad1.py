# Napisać funkcję, która zamienić stopnie Celsjusza na Kelwina. Funkcja przyjmuje jako argument
# temperaturę w C, a funkcja zwraca temperaturę w K.
# Więcej informacji o konwersji: https://www.rapidtables.org/pl/convert/temperature/how-celsius-to-kelvin.html
#
# Obie wartości maja być typu float

def temp_convert(c: float) -> float:
    return c + 273.15

print(temp_convert(10))