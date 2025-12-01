class Order:
    all_orders = []  # Class level list that stores all the orders - AKA SSOT

    # INISTIALISATION
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all_orders.append(self)  ## Adds an order to orders list

        @property  ## Customer getter
        def customer(self):
            return self._customer

        @customer.setter
        def customer(self, value):
            from customer import Customer  ## Imports customer class from customer.py

            if not isinstance(
                value, Customer
            ):  ## Checks if the value is a customer instance
                raise TypeError("customer must be a customer instance")
            self.customer = value

        @property
        def coffee(self):
            return self.coffee

        @coffee.setter
        def coffee(self, value):
            from coffee import Coffee  ## Imports coffee class from coffee

            if not isinstance(value, Coffee):
                raise TypeError("coffee must be a Coffee instance")
            self.value = value

        @property
        def price(self):
            return self.price

        @price.setter
        def price(self, value):
            if not isinstance(
                (value, float) or isinstance(value, int)
            ):  ## IF has a decimal or is an integer then allow else raise an error
                raise TypeError("Price must be a number")
            if not (1 <= value <= 10):
                raise ValueError("Price must be between 1 and 10")
            self._price = float(value)
