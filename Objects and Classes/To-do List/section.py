from task import Task


class Section:
    def __init__(self, name):
        self.name = name

        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"

        self.tasks.append(new_task)

        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        for task in self.tasks:
            if task.name == task_name:
                task.set_completed()
                return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        amount = 0
        for task in self.tasks:
            if task.get_completed():
                self.tasks.remove(task)
                amount += 1

        return f"Cleared {amount} tasks."

    # function reaches the end without a return statement, so by default, Python returns None.
    def view_section(self):
        result = [f"Section {self.name}:"]

        for task in self.tasks:
            result.append(task.details())

        return "\n".join(result)
