def reverse_text(text):
    size = len(text) -1
    for t in range(size, -1, -1):
        yield text[t]

for char in reverse_text("step"):
    print(char, end="")
