import calendar


class DVD:
    DEFAULT_RENTED = False
    def __init__(self, name: str, id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name= name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = DVD.DEFAULT_RENTED

    @staticmethod
    def from_date(id: int, name: str, date: str, age_restriction: int):
        str_data = date.split('.')
        creation_year = int(str_data[2])
        creation_month = calendar.month_name[int(str_data[1])]

        return DVD(name, id, creation_year, creation_month, age_restriction)

    def __repr__(self):
        status = "rented" if self.is_rented else "not rented"
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction {self.age_restriction}. Status: {status}"
