def removeVowels(text, vowels):
    size = len(vowels)
    
    # string is immutable - i need list
    text_list = list(text)
    
    for character in text:
        for i in range(0, size, 1):
            character_lower = character.lower()
            if character_lower== vowels[i]:
                # original uppercase character (e.g. "I" becomes "i"). -if i use  character = character.lower()
                # Later when  call text_list.remove(character) - trying to remove lowercase 'i' from a list that actually contains uppercase 'I'. Because of this i use character_lower = character.lower() instead of character = character.lower()
                text_list.remove(character)
    
    return ''.join(text_list)            

vowels = ['a', 'o', 'u', 'e', 'i']

text = input()

text = removeVowels(text, vowels)

print(text)