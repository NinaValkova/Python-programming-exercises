from customer import Customer
from dvd import DVD


class MovieWorld:
    DVD_CAPACITY = 15
    CUSTOMER_CAPACITY = 10

    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.dvds = []

    @classmethod
    def dvd_capacity(cls):
        return cls.DVD_CAPACITY

    @classmethod
    def customer_capacity(cls):
        return cls.CUSTOMER_CAPACITY

    def add_customer(self, customer: Customer):
        size = len(self.customers)
        customer_capacity = self.customer_capacity()
        if customer_capacity > size:
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        size = len(self.dvds)
        dvd_capacity = self.dvd_capacity()
        if dvd_capacity > size:
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        
        # (d for d in self.dvds if d.id == dvd_id)
        # This is a generator expression — it goes through every d (each DVD object) inside the list self.dvds and filters only those where d.id == dvd_id.
        # So it’s like saying: “Find all DVDs whose ID matches dvd_id.”
        # But instead of creating a new list, it generates items one by one.
        
        # next(...)
        # The built-in function next() retrieves the first item from a generator.
        # So here it means: “Give me the first DVD in self.dvds with that ID.”
        dvd = next((d for d in self.dvds if d.id == dvd_id), None)
        if dvd is not None:
            for customer in self.customers:
                # Find the specific customer
                if customer.id == customer_id:
                    if dvd in customer.rented_dvds:
                        return f"{customer.name} has already rented {dvd.name}"
                    if dvd.is_rented:
                        return "DVD is already rented"
                    if customer.age < dvd.age_restriction:
                        return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
                    customer.rented_dvds.append(dvd)
                    dvd.is_rented = True
                    return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        dvd = next((d for d in self.dvds if d.id == dvd_id), None)
        if dvd is not None:
            for customer in self.customers:
                if customer.id == customer_id and dvd in customer.rented_dvds:
                    customer.rented_dvds.remove(dvd)
                    dvd.is_rented = False
                    return f"{customer.name} has successfully returned {dvd.name}"
            return f"{customer.name} does not have that DVD"

    def __repr__(self):
        result = ""
        for customer in self.customers:
            result += customer.__repr__() + "\n"

        for dvd in self.dvds:
            result += dvd.__repr__() + "\n"

        return result
