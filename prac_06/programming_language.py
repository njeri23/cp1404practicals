class ProgrammingLanguage:
    """Represent a ProgrammingLanguage object."""

    def __init__(self, name, typing, reflection, year):
        """Initialise a ProgrammingLanguage instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return whether the language is dynamically typed."""
        return self.typing == "Dynamic"

    def __str__(self):
        """Return a string representation of the language."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
