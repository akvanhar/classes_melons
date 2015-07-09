"""This file should have our melon-type classes in it."""
class Melons(object):
    base_price = 1.0

class WatermelonOrder(Melons):
    species = "Watermelon"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Fall', 'Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        if qty < 3:
            total = qty * self.base_price
        else:
            total = qty * (self.base_price*0.75)

        return total

class CantaloupeOrder(Melons):
    species = "Cantaloupe"
    color = "tan"
    imported = False
    shape = "natural"
    seasons = ['Spring', 'Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        if qty < 5:
            total = qty * self.base_price
        else:
            total = qty * (self.base_price / 2.0)

        return total

class CasabaOrder(Melons):
    species = "Casaba"
    color = "green"
    imported = True
    shape = "natural"
    seasons = ["Spring", "Summer", "Fall", "Winter"]

    def get_price(self,qty):
        """Calculate price, given a number of melons ordered."""
        total = qty * (self.base_price + 1) * 1.5

        return total

class SharlynOrder(Melons):
    species = "Sharlyn"
    color = "tan"
    imported = True
    shape = "natural"
    seasons = ["Summer"]

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        total = qty * self.base_price * 1.5
        return total

class SantaClausOrder(Melons):
    species = "Santa Claus"
    color = "green"
    imported = True
    shape = "natural"
    seasons = ["Winter", "Spring"]

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        total = qty * self.base_price * 1.5
        return total

class ChristmasOrder(Melons):
    species = "Christmas"
    color = "green"
    imported = "False"
    shape = "natural"
    seasons = ["Winter"]

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        total = qty * self.base_price
        return total

class HornedMelonOrder(Melons):
    species = "Horned Melon"
    color = "yellow"
    imported = True
    shape = "natural"
    seasons = ["Summer"]

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        total = qty * self.base_price
        return total

class XiguaOrder(Melons):
    species = "Xigua"
    color = "black"
    imported = True
    shape = "square"
    seasons = ["Summer"]

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        total = qty * self.base_price * 2 * 1.5
        return total

class OgenOrder(Melons):
    species = "Ogen"
    color = "tan"
    imported = False
    shape = "natural"
    seasons = ["Spring", "Summer"]

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        total = qty * (self.base_price + 1.0)
        return total

