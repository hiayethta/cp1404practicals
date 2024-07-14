"""CP1404 - ProgrammingLanguage class"""


class ProgrammingLanguage:
    # Initialise row names from Programming Language Comparison page
    def __init__(self, field="", typing="", reflection="", year=0):
        self.field = field
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        if self.typing == "Dynamic":
            return True
        else:
            return False

