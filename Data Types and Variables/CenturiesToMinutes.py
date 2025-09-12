# def days_in_year(year: int) -> int:
#     if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#         return 366
#     return 365


# centuries = int(input())
# years = centuries * 100

# days = 0
# for year in range(1, years + 1):
#     days += days_in_year(year)

# hours = days * 24
# minutes = hours * 60

# print(f"{centuries} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes")


centuries = int(input())

years = centuries * 100
days = int(years * 365.2422)
hours = int(days * 24)
minutes = int(hours * 60)

print(f"{centuries} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes")
