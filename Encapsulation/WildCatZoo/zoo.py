class Zoo:

    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if len(self.animals) >= self.__animal_capacity:
            return "Not enough space for animal"
        if self.__budget < price:
            return "Not enough budget"

        self.animals.append(animal)
        self.__budget -= price

        return f"{animal.name} the {type(animal).__name__} added to the zoo"

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {type(worker).__name__} hired successfully"

        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)

                return f"{worker_name} fired successfully"

        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salaries = sum(worker.salary for worker in self.workers)
        if total_salaries <= self.__budget:
            self.__budget -= total_salaries
            return (
                f"You payed your workers. They are happy. Budget left: {self.__budget}"
            )
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_cost = sum(animal.money_for_care for animal in self.animals)
        if total_cost <= self.__budget:
            self.__budget -= total_cost
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        count = len(self.animals)

        result = [f"You have {count} animals"]

        # __repr__() = defines how an object looks as a string
        lions = [
            repr(animal) for animal in self.animals if type(animal).__name__ == "Lion"
        ]
        tigers = [
            repr(animal) for animal in self.animals if type(animal).__name__ == "Tiger"
        ]
        cheetahs = [
            repr(animal)
            for animal in self.animals
            if type(animal).__name__ == "Cheetah"
        ]

        result.append(f"----- {len(lions)} Lions:")
        result.extend(lions)
        result.append(f"----- {len(tigers)} Tigers:")
        result.extend(tigers)
        result.append(f"----- {len(cheetahs)} Cheetahs:")
        result.extend(cheetahs)

        return "\n".join(result)

    def workers_status(self):
        count = len(self.workers)

        result = [f"You have {count} workers"]

        keepers = [
            repr(keeper) for keeper in self.workers if type(keeper).__name__ == "Keeper"
        ]
        caretakers = [
            repr(caretaker)
            for caretaker in self.workers
            if type(caretaker).__name__ == "Caretaker"
        ]
        vets = [repr(vet) for vet in self.workers if type(vet).__name__ == "Vet"]

        result.append(f"----- {len(keepers)} Keepers:")
        result.extend(keepers)
        result.append(f"----- {len(caretakers)} Caretakers:")
        result.extend(caretakers)
        result.append(f"----- {len(vets)} Vets:")
        result.extend(vets)

        return "\n".join(result)
