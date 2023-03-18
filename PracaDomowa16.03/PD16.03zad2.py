# Napisać funkcję, która jako argument przyjmuje dowolny łańcuch znakowy, a następnie zwraca
# słownik zliczający ilość wystąpień każdego słowa (kot =/= kota). Podpowiedź możemy użyć metody split(" ").

def calc_words(text) -> dict:
    word_calc = {}
    for word in text.lower().split(" "):
        if word  in word_calc.keys():
            word_calc[word] += 1
        else:
            word_calc[word] = 1
    return word_calc

print(calc_words("hello how are you are you ok"))