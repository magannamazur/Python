# Użytkownik podaje liczbe całkowitą. Następnie program zwraca sumę CYFR z których składa się
# podana liczba. Przykładowo: użytkownik podaje 1307, program zwraca 11 (1+3+0+7).
# Podpowiedź: konwersja na str

text = str(input("Podaj liczbe:"))
i = 0
suma = 0
while i < len(text):
    suma += int(text[i])
    i += 1

print(suma)
