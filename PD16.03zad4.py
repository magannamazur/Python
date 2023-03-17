# Napisać program, gdzie użytkownik podaje liczby całkowite i je sumuje. Program działa dopóki
# użytkownik nie poda liczby ujemnej. Po podaniu liczby ujemnej program wyświetla sumę podanych poprzednich liczb.

neg_check = True
suma = 0

while neg_check:
    a = int(input("Podaj liczbe:"))
    if a >= 0:
        suma += a
    else:
        neg_check = False

print(suma)