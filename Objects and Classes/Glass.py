class Glass:
    capacity = 250  # class attribute

    def __init__(self):
        self._content = 0  # instance attribute

    @property
    def content(self):
        return self._content  

    @content.setter
    def content(self, content):
        self._content = content

    def fill(self, ml):
        if Glass.capacity > self.content + ml:
            self.content += ml
            return f"Glass filled with {ml} ml"
        return f"Cannot add {ml} ml"

    def empty(self):
        self.content = 0
        return "Glass is now empty"

    def info(self):
        size = Glass.capacity - self.content
        return f"{size} ml left"


glass = Glass()
print(glass.fill(100))
print(glass.fill(200))
print(glass.empty())
print(glass.fill(200))
print(glass.info())
