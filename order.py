class Order:
    all_orders = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all_orders.append(self)

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, value):
        from customer import Customer

        if not isinstance(value, Customer):
            raise TypeError("customer must be a Customer instance")
        self._customer = value  # <-- use private variable

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, value):
        from coffee import Coffee

        if not isinstance(value, Coffee):
            raise TypeError("coffee must be a Coffee instance")
        self._coffee = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, (float, int)):
            raise TypeError("Price must be a number")
        if not (1 <= value <= 10):
            raise ValueError("Price must be between 1 and 10")
        self._price = float(value)
