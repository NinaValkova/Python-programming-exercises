class Party:
    def __init__(self):
        self.__names = []
        
    @property
    def Names(self):
        return self.__names
    
    @Names.setter
    def Names(self, names):
        self.__names = names


class ReadInput:
    @staticmethod
    def read_input(party):
        names = []
        name = input()
        while name != 'End':
            names.append(name)
            name = input()

        party.Names = names  
        return names    

class PrintInput:
    @staticmethod
    def print_input(names):
        counter = 0
        names_formatted = []
        size = len(names)
        for i in range(0, size):
            names_formatted.append(names[i])
            counter +=1

        print(f"Going: {', '.join(names_formatted)}")
        return counter    

party = Party()
names = ReadInput.read_input(party)

total_names = PrintInput.print_input(names)
print(f"Total: {total_names}")
