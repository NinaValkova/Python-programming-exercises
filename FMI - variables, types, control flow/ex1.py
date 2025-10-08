# Задача 1
# Създайте функция, която приема число, указващо брой секунди и го връща трансформирано в наредена тройка от часове, минути и секунди.

# Например

# 3661 -> (1, 1, 1), понеже 3661 секунди са 1hr 1min 1sec.
# 86399 -> (23, 59, 59), понеже 86399 секунди са 23hr 59min 59sec. и т.н.

max_hours = 24

hour_to_sec = 3600
minute_to_sec = 60


def seconds_to_time(time):

    hours = (time // hour_to_sec) % max_hours
    minutes = (time % hour_to_sec) // minute_to_sec
    seconds = time % minute_to_sec

    return (hours, minutes, seconds)


print(seconds_to_time(0) == (0, 0, 0))
print(seconds_to_time(1) == (0, 0, 1))
print(seconds_to_time(69) == (0, 1, 9))
print(seconds_to_time(420) == (0, 7, 0))
print(seconds_to_time(3661) == (1, 1, 1))
print(seconds_to_time(86399) == (23, 59, 59))
