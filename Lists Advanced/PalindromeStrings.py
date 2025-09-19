def find_palindromes(words):
    palindromes = []
    
    for word in words:
        #reverse_word = word[::-1]
        reverse_word = ''.join(reversed(word))
        if word == reverse_word:
            palindromes.append(word)
    
    return palindromes       
 
def find_occurrences(unique_word, palindromes):
     occurrences = 0
     
     for word in palindromes:
         if word == unique_word:
             occurrences += 1
    
     return occurrences    

line = input()
unique_word = input()

words = line.split()

palindromes = find_palindromes(words)
print(palindromes)
occurrences = find_occurrences(unique_word, palindromes)
print(f'Found palindrome {occurrences} times')

