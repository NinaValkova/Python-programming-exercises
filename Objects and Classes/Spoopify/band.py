from album import Album


class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        for a in self.albums:
            if a.name == album.name:
                return f"Band {self.name} already has {album.name} in their library."

        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        for a in self.albums:
            if a.name == album_name:
                if a.is_published():
                    return "Album has been published. It cannot be removed."
                self.albums.remove(a)
                return f"Album {album_name} has been removed."
        
        return f"Album {album_name} is not found."

    def details(self):
        result = [f"Band {self.name}"]

        for album in self.albums:
            result.append(album.details())

        return "\n".join(result)
