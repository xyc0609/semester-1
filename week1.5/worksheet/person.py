# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """
    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)
    
    def __init__(self, name, birth):
        """
        Initialialise a Person with aname and date of birth.
        """
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if name == "":
            raise ValueError("name cannot be empty")
        if not isinstance(birth, date):
            raise TypeError("birth must be a date")

        self.name = name
        self.birth = birth

    def initials(self):
        """
        Return the uppercase initials of the person's name.
        """
        return "".join(word[0].upper() for word in self.name.split())
    
    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)
    def is_birthday(self):
        """
        Return True if ttoday is the person's birthday.
        """
        today = date.today()
        return (today.month, today.day) == (self.birth.month, self.birth.day)