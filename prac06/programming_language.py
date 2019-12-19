class ProgrammingLanguage:
    """Represents Programming Language object"""
    def __init__(self, name, typing, reflection, year):
        """Initialise language instance"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """returns string representative of object"""
        return "{}, {} Typing, Reflection = {}, First appeared in {}".format(self.name, self.typing, self.reflection,
                                                                             self.year)

    def is_dynamic(self):
        """Checks if language is dynamically typed"""
        return self.typing == "Dynamic"

