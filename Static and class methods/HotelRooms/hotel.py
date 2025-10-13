from room import Room


class Hotel:
    DEFAULT_GUESTS = 0

    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = Hotel.DEFAULT_GUESTS

    @staticmethod
    def from_stars(stars_count: int):
        return Hotel(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        for room in self.rooms:
            if room.number == room_number:
                room.take_room(people)

    def free_room(self, room_number):
        for room in self.rooms:
            if room.number == room_number:
                room.free_room()

    def status(self):
        self.guests = sum(r.guests for r in self.rooms)

        result = [f"Hotel {self.name} has {self.guests} total guests"]
        free_rooms = [str(r.number) for r in self.rooms if not r.is_taken]
        taken_rooms = [str(r.number) for r in self.rooms if r.is_taken]

        result.append(f"Free rooms: {', '.join(free_rooms)}")
        result.append(f"Taken rooms: {', '.join(taken_rooms)}")

        return "\n".join(result)
