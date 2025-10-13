class Room:
    DEFAULT_GUESTS = 0
    DEFAULT_TAKEN = False

    def __init__(self, number, capacity):
        self.number = number
        self.capacity = capacity
        self.guests = Room.DEFAULT_GUESTS
        self.is_taken = Room.DEFAULT_TAKEN

    def take_room(self, people):
        if self.is_taken or self.capacity < people:
            return f"Room number {self.number} cannot be taken"

        self.is_taken = True
        self.guests = people

    def free_room(self):
        if self.is_taken:
            self.is_taken = Room.DEFAULT_TAKEN
            self.guests = Room.DEFAULT_TAKEN

        return f"Room number {self.number} is not taken"
