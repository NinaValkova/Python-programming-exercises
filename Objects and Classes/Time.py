# class Time:
#     max_hours = 24
#     max_minutes = 60
#     max_seconds = 60

#     def __init__(self, hours, minutes, seconds):
#         self.hours = hours
#         self.minutes = minutes
#         self.seconds = seconds

#     def set_time(self, hours, minutes, seconds):
#         self.hours = (hours + minutes // Time.max_minutes) % Time.max_hours
#         self.minutes = minutes % Time.max_minutes

#         if seconds >= 60:
#             self.minutes += seconds // Time.max_seconds
#             self.seconds = seconds % Time.max_seconds
#         else:
#             self.seconds = seconds

#         if self.minutes >= Time.max_minutes:
#             self.hours = (self.hours + self.minutes // Time.max_minutes) % Time.max_hours
#             self.minutes = self.minutes % Time.max_minutes

#     def get_time(self):
#         return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

#     def next_second(self):
#         self.seconds += 1
#         self.set_time(self.hours, self.minutes, self.seconds)

#         return self.get_time()


# time = Time(10, 59, 59)
# print(time.next_second())


class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        # Format the value of self.hours as an integer (d) with at least 2 digits,
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def next_second(self):
        self.seconds += 1

        if self.seconds >= Time.max_seconds:
            self.minutes += 1
            self.seconds = 0

        if self.minutes >= Time.max_minutes:  
            self.hours += 1
            self.minutes = 0  

        if self.hours >= Time.max_hours:
            self.hours = 0    

        return self.get_time()


time = Time(9, 30, 59)
print(time.next_second())
