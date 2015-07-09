"""This file should have our melon-type classes in it."""
class _Melons(object):
    base_price = 5.0

    def __new__(cls):
        if cls is _Melons:
            raise TypeError("You can't sell plain melons")
        return object.__new__(cls)

    def get_price(self, qty):
        print "HEY SALESPERSON!!! You can't sell a PLAIN melon!"

class WatermelonOrder(_Melons):
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

class CantaloupeOrder(_Melons):
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

class CasabaOrder(_Melons):
    species = "Casaba"
    color = "green"
    imported = True
    shape = "natural"
    seasons = ["Spring", "Summer", "Fall", "Winter"]

    def get_price(self,qty):
        """Calculate price, given a number of melons ordered."""
        total = qty * (self.base_price + 1) * 1.5

        return total

class SharlynOrder(_Melons):
    species = "Sharlyn"
    color = "tan"
    imported = True
    shape = "natural"
    seasons = ["Summer"]

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        total = qty * self.base_price * 1.5
        return total

class SantaClausOrder(_Melons):
    species = "Santa Claus"
    color = "green"
    imported = True
    shape = "natural"
    seasons = ["Winter", "Spring"]

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        total = qty * self.base_price * 1.5
        return total

class ChristmasOrder(_Melons):
    species = "Christmas"
    color = "green"
    imported = "False"
    shape = "natural"
    seasons = ["Winter"]

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        total = qty * self.base_price
        return total

class HornedMelonOrder(_Melons):
    species = "Horned Melon"
    color = "yellow"
    imported = True
    shape = "natural"
    seasons = ["Summer"]

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        total = qty * self.base_price
        return total

class XiguaOrder(_Melons):
    species = "Xigua"
    color = "black"
    imported = True
    shape = "square"
    seasons = ["Summer"]

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        total = qty * self.base_price * 2 * 1.5
        return total

class OgenOrder(_Melons):
    species = "Ogen"
    color = "tan"
    imported = False
    shape = "natural"
    seasons = ["Spring", "Summer"]

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        total = qty * (self.base_price + 1.0)
        return total

