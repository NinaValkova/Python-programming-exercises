# def getString(number:int, line:str):

#     return line*number

line = input()

number = int(input())

# repeating_string = getString(number, line)
# print(repeating_string)

repeat_string = lambda number, line: line * number

print(repeat_string(number, line))