line = input()

decipher_messages = []
messages = line.split()
ascii = ''
for message in messages:
    size = len(message)
    for i in range(0, size, 1):
        if message[i].isdigit():
            ascii+=message[i]
        else:
            break    
    letters_count = len(ascii)    
    message_decoded =  chr(int(ascii)) +  message[letters_count:]
    
    message_decoded = list(message_decoded)
    message_decoded[1], message_decoded[-1] =message_decoded[-1],  message_decoded[1]
    
    message_decoded =''.join(message_decoded)
    decipher_messages.append(message_decoded)
    
    ascii = ''

for message in decipher_messages:
    print(message, end=' ')    