import math

class PhotoAlbum:
    MAX_PHOTOS = 4
    def __init__(self, pages):
        self.pages = pages

        # list comprehension that creates the photos attribute as a list of empty lists
        self.photos = [[] for _ in range(pages)]

    @staticmethod
    def from_photos_count(photos_count: int):
        curr_pages_count  = math.ceil(photos_count / PhotoAlbum.MAX_PHOTOS)

        return PhotoAlbum(curr_pages_count)

    def add_photo(self, label: str):
        page_number = 0
        slot_number = 0
        for i in range(0, self.pages):
            if len(self.photos[i]) < PhotoAlbum.MAX_PHOTOS:
                self.photos[i].append(label)
                page_number = i + 1
                slot_number = len(self.photos[i])

                return f"{label} photo added successfully on page {page_number} slot {slot_number}"

        return "No more free slots"

    def display(self):
        photo_symbol = '[]' 
        page_separation = '-' * 11

        result = page_separation + '\n'
        for page in self.photos:
            if page:
                result += " ".join([photo_symbol] * len(page)) + '\n'
            else:    
                result += '\n'
            result +=  page_separation + "\n"

        return result      


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
