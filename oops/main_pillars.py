class Item:

    def __init__(self, title, daily_fee, days_borrowed=0):
        self.title = title
        self.daily_fee = daily_fee
        self.days_borrowed = days_borrowed

    @property
    def daily_fee(self):
        return self._daily_fee

    @daily_fee.setter
    def daily_fee(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("daily_fee must be a number")
        if value < 0:
            raise ValueError("daily_fee must be >= 0")
        self._daily_fee = float(value)

    @property
    def days_borrowed(self):
        return self._days_borrowed

    @days_borrowed.setter
    def days_borrowed(self, value):
        if not isinstance(value, int):
            raise TypeError("days_borrowed must be int")
        if value < 0:
            raise ValueError("days_borrowed must be >= 0")
        self._days_borrowed = value

    def cost(self) -> float:
        return self.daily_fee * self.days_borrowed


class Book(Item):

    def __init__(self, title, author, daily_fee, days_borrowed=0):
        super().__init__(title, daily_fee, days_borrowed)
        self.author = author


class DVD(Item):

    def __init__(self, title, age_rating, daily_fee, days_borrowed=0):
        super().__init__(title, daily_fee, days_borrowed)
        self.age_rating = age_rating

    def cost(self) -> float:
        return super().cost() + 1.50


def total_cost(items) -> float:
    total = 0.0
    for item in items:
        total += item.cost()
    return total
