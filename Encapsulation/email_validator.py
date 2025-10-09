class EmailValidator:
    def __init__(self, min_length, mails, domains):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    @property
    def min_length(self):
        return self.__min_length

    @min_length.setter
    def min_length(self, min_length):
        self.__min_length = min_length

    @property
    def mails(self):
        return self.__mails

    @property
    def domains(self):
        return self.__domains

    @domains.setter
    def domains(self, domains):
        self.__domains = domains

    @mails.setter
    def mails(self, mails):
        self.__mails = mails

    def __is_name_valid(self, name):
        length = len(name)

        if length < self.min_length:
            return False   

        return True 

    def __is_mail_valid(self, mail):
        if mail not in self.mails:
            return False

        return True 

    def __is_domain_valid(self, domain):
        if domain not in self.domains:
            return False

        return True    

    def validate(self, email):
        name, line = email.split("@")

        mail, domain = line.split(".")

        return self.__is_name_valid(name) and self.__is_mail_valid(mail) and self.__is_domain_valid(domain)


mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))
