# Napisać funkcję, która jako argument przyjmuje dowolny łańcuch znakowy, a następnie zwraca
# słownik zliczający ilość wystąpień każdego słowa (kot =/= kota). Podpowiedź możemy użyć metody split(" ").

def calc_words(text) -> dict:
    word_calc = {}
    for word in text.split(" "):
        if word not in word_calc.keys():
            word_calc[word] = text.count(word)
    return word_calc

print(calc_words("hello how are you? are you ok?"))