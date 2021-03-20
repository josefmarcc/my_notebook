class InvalidArgumentException(Exception):
    pass


class Person():
    """A simple class to create a person with a name and 
    making sure that the persons name is uppercase and only contains letters"""

    def __init__(self, name):
        if name.isalpha() and name[0].isupper():
            print("Name is all letters and has a capital letter")
            self.name = name
        else:
            raise InvalidArgumentException()


true_person = Person("Frederik")
print(true_person.name)
false_person = Person("1234")
print(false_person.name)
