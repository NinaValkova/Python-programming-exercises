def read_notes():
    notes = []
    note = ''
    
    note = input()
    while note != 'End':
        importance, note = note.split('-')
        notes.append((int(importance), note))
        
        note = input()
        
    return notes    

def printNotes(notes):
    notes.sort(key=lambda x:x[0])
    
    note = [note[1] for note in notes]
    
    print(note)


notes = read_notes()

printNotes(notes)