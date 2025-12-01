from order import Order


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

    def order(self):
        return [
            order for order in Order.all_orders if order.customer is self
        ]  ## Returns order is order belongs to said customer

    def coffees(self):
        unique_list = set()  # Ensures uniqueness as customer - No duplicates
        for order in self.orders():  ## For orders belonging to the customer
            unique_list.add(order.coffee)  ## Add the coffee to unique list
        return list(unique_list)  ## REturns a unique list of customers orders

    def create_order(self, coffee, price):
        from order import Order  ## Import inside method to avoid circular imports

        return Order(self, coffee, price)

    def num_orders(self):
        return len(self.orders())


def average_price(self):
    orders = self.orders()
    if not orders:
        return 0
    return sum(order.price for order in orders) / len(orders)


@classmethod
def most_aficionado(cls, coffee):
    from order import Order

  #Keep track of how much each customer spent on this coffee
    spend = {}

    # Loop through all orders
    for order in Order.all_orders:
        
        if order.coffee is coffee:
            customer = order.customer
            # Add this order's price to the customer's total
            if customer in spend:
                spend[customer] += order.price
            else:
                spend[customer] = order.price


    # customer who spent the most
    most = None
    highest = 0
    for customer, total in spend.items():
        if total > highest:
            highest = total
            most = customer

    #  Return that customer
    return most
