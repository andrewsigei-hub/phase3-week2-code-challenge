class Customer:
    def __init__(self, name):
        self.name = name

        @property  # Getter method
        def name(self):
            return self._name

        @name.setter  # Setter method
        def name(self, new_name):
            if not isinstance(new_name, str):  ## Checks whether input name is string
                raise TypeError("Name must be a string")
            if (
                len(name) > 1 and len(name) < 15
            ):  ## Validation that check length of name string
                self._name = new_name
            else:
                raise ValueError("Name must have 1-15 characters")
