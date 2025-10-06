class Person:
    def __init__(self, name):
        self.Name = name

    # Now you access the .Name property of the Person object
    @property
    def Name(self):
        return self._name

    @Name.setter
    def Name(self, name):
        self._name = name


class Message:
    def __init__(self, content):
        self.Content = content

    @property
    def Content(self):
        return self._content

    @Content.setter
    def Content(self, content):
        self._content = content


# email.Sender  # calls Email.Sender -> returns Person("John")
# email.Sender.Name  # calls Person.Name -> returns "John"
class Email:
    def __init__(self, sender, receiver, content):
        self.Sender = sender
        self.Receiver = receiver
        self.Content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.Sender.Name} says to {self.Receiver.Name}: {self.Content.Content}. Sent: {self.is_sent}"

    # returns the Person object
    @property
    def Sender(self):
        return self._sender

    @Sender.setter
    def Sender(self, sender):
        self._sender = sender

    @property
    def Receiver(self):
        return self._receiver

    @Receiver.setter
    def Receiver(self, receiver):
        self._receiver = receiver

    @property
    def Content(self):
        return self._content

    @Content.setter
    def Content(self, content):
        self._content = content


class ReadInput:
    @staticmethod
    def read_input():
        command = input()

        mailbox = Mailbox()
        while command != "Stop":
            command = command.split(" ")

            sender = Person(command[0])
            receiver = Person(command[1])
            content = Message(command[2])

            email = Email(sender, receiver, content)
            mailbox.add_email((email))

            command = input()

        return mailbox

    @staticmethod
    def read_indices():
        command = input()

        indices = [int(x) for x in command.split(", ")]
        return indices


class Mailbox:
    def __init__(self):
        self._emails = []

    def add_email(self, email):
        self._emails.append(email)

    def print_emails(self):
        for email in self._emails:
            print(email.get_info())

    def send_email(self, indices):
        for i in indices:
            self._emails[i].send()


mailbox = ReadInput.read_input()
indices = ReadInput.read_indices()
mailbox.send_email(indices)
mailbox.print_emails()
