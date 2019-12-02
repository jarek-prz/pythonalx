class Employee:

    def __init__(self, name, last_name, rate_per_hour):
        self.name = name
        self.last_name = last_name
        self.rate_per_hour=rate_per_hour
        self.registered_hours = 0

    def register_time(self, time):
        self.registered_hours = time

    def pay_salary(self):
        if self.registered_hours<=8:
            to_pay= self.registered_hours * self.rate_per_hour
        else:
            to_pay = (8 * self.rate_per_hour) + (self.registered_hours -8) * (self.rate_per_hour * 2)
        self.registered_hours =0
        return to_pay

# __registered_hours jest prywatny - 2 podkreślenia
