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

class Bonus:
    def __init__(self, value):
        self.value = value

class AmountBonus (Bonus):
    pass

class PercentBonus (Bonus):
    pass

class Premium_employee(Employee):
    def __init__(self, f_name, l_name, rph):
        super().init(f_name, l_name, rph)
        self.bonuses=[]

    def give_bonus(self, bonus):
        self.bonuses.append(bonus)

    def pay_salary(self):
        s=super().pay_salary() + self.bonus
        to_pay = super().pay_salary()
        amount_bonuses = sum([x.value for x in self.bonuses if isinstance(x, AmountBonus)])
        percent_bonuses = sum([x.value for x in self.bonuses if isinstance(x, PercentBonus)])
        to_pay = to_pay + (to_pay * percent_bonuses ) / 100
        amount_bonuses=[]
        percent_bonuses=[]
        return to_pay





