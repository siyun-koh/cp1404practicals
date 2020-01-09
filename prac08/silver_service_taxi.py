from prac08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        """overwritten Taxi __init__ with fanciness attribute."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string like a Taxi object but with additional flagfall charge."""
        return "{} plus flagfall of ${:.2f}".format(super().__str__(), self.flagfall)

    def get_fare(self):
        """overwritten from Taxi to include flagfall attribute."""
        return self.flagfall + super().get_fare()
