# Example
# Input	Output
# a b c d e f g h
# 5	['a', 'c', 'e', 'g', 'b', 'd', 'f', 'h']

# Initially, the deck is ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'].

# After 1st faro shuffle: ['a', 'e', 'b', 'f', 'c', 'g', 'd', 'h']

# After 2nd faro shuffle: ['a', 'c', 'e', 'g', 'b', 'd', 'f', 'h']

# After 3rd faro shuffle: ['a', 'e', 'c', 'g', 'b', 'f', 'd', 'h']

# After 4th faro shuffle: ['a', 'c', 'e', 'g', 'b', 'd', 'f', 'h']

# After 5th faro shuffle: ['a', 'c', 'e', 'g', 'b', 'd', 'f', 'h']



def faro_shffle(cards):
    half_size = len(cards) // 2
    first_half = cards[:half_size]
    second_half = cards[half_size:]

    shuffled_cards = []
    for i in range(0, half_size, 1):
        shuffled_cards.append(first_half[i])
        shuffled_cards.append(second_half[i])

    return shuffled_cards    


line = input()
suffle_count = int(input())

cards = line.split()

for i in range(0,suffle_count, 1):
    cards = faro_shffle(cards)

print(cards)
