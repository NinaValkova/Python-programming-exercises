# Задача 2
# Създайте функция, която да връща броя на гласните в даден текст (нека за улеснение считаме за гласни само a, e, i, o, u).


def number_of_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    counter = 0
    text = text.lower()
    for letter in text:
        if letter in vowels:
            counter +=1

    return counter


print(number_of_vowels("grrrrgh!") == 0)
print(number_of_vowels("The quick brown fox jumps over the lazy dog.") == 11)
print(number_of_vowels("MONTHY PYTHON") == 2)
