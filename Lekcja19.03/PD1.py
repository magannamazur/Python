# Zadanie 01
#
# Napisz funkcję, która jak argument przyjmuje listę liczby całkowitych, a zwraca wartość int jako największa liczba
# z listy (nie wolno używać max).
#
# Dodatkowo zabezpiecz program, przed błednymi danymi (np. tekst)

def find_max(lista: list) -> int:
    result = 0
    for i in lista:
        # try
        #     lista[i-1]
        # expect
        try:
            if lista[i-1] > result:
                result = lista[i - 1]
        except TypeError:
            continue
    return result


print(find_max([1,2,3,"gfh",5,6]))