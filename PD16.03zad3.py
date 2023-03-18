# Użytkownik podaje trzy liczby całkowite. Następnie program zwraca informację, która z podanych liczb
# jest największa (dla odważnych - możecie również weryfikować czy dane liczbą są takie same).

a,b,c = str(input("Podaj 3 liczby:")).split(" ")
a = int(a)
b = int(b)
c = int(c)

if a > b:
    biggest = a
    if a < c:
        biggest = c
else:
    biggest = b
    if b < c:
        biggest = c

print(f"Największa liczba to: {biggest}")

print(f"Największa liczba to: {max([a,b,c])}")