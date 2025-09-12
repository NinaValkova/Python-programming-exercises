start = int(input())
end = int(input())

for i in range(start, end + 1, 1):
    letter = chr(i) # Return the string representing a character with the specified Unicode code point
    print(letter, end = " ")