class Person:
    def __init__(self):
        print("Second Call")
        print('Creating an instance of Person')
        # address
        self.name = None
        self.position = None
        self.date_of_birth = None

    def __str__(self):
        print("Seventh Call")
        return f"{self.name} born on {self.date_of_birth} works as {self.position}"


class PersonBuilder:
    def __init__(self):
        print("First Call")
        self.person = Person()

    def build(self):
        print("Sixth Call")
        return self.person


class PersonInfoBuilder(PersonBuilder):
    def called(self, name):
        print("Third Call")
        self.person.name = name
        return self


class PersonJobBuilder(PersonInfoBuilder):
    def works_as_a(self, position):
        print("Fourth Call")
        self.person.position = position
        return self


class PersonDateBuilder(PersonJobBuilder):
    def born(self, date_of_birth):
        print("Fifth Call")
        self.person.date_of_birth = date_of_birth
        return self


if __name__ == '__main__':
    pb = PersonDateBuilder()
    me = pb.called("mahesh").works_as_a("quant").born("1/1/1980").build()
    print(me)
