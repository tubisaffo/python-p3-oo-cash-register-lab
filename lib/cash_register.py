#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount = 0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction = ()
        
    def add_item(self, title, price, quantity = 1):
        self.total += price * quantity
        self.last_transaction = (title, price, quantity)
        for i in range(0, quantity):
            self.items.append(title)

    def apply_discount(self):
        if self.discount > 0:
            self.total -= int((self.discount/100) * self.total)
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if len(self.items) > 0:
            self.total -= self.last_transaction[1] * self.last_transaction[2]
            self.items.pop()
        else:
            print("There are no items to void.")