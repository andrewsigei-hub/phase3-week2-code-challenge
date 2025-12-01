from order import Order


class Coffee:
    def __init__(self, name):  ## Initializor
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

    def orders(self):
        [
            order for order in Order.all_orders if order.coffee is self
        ]  ## For all orders inside ssot if the order is that specific coffee instance add it to the new list and return the list

    def customers(self):
        customers = set() # Used a set to remove duplicates in order to get a unique list of customers who ordered that coffee
        for order in self.orders(): # In all the orders get orders belonging to this coffee
            customers.add(order.customer)
            return list(customers) # Convert back to list and return, list only shows customer name once
    

