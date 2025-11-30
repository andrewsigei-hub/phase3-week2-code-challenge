class Coffee:
    def __init__(self, name): ## Initializor
        self._name = name

    @property  # Getter method
    def name(self):
        return self._name

    @name.setter  # Coffee setter method
    def name(self, new_coffee):
        if not isinstance(new_coffee, str):
            raise TypeError("Coffee name must be string")  # Type validator

        if len(new_coffee) >= 3:
            self._name = new_coffee
        else:
            raise ValueError(
                "Coffee must be greater than 3 characters"
            )  # Value validator
