from ODP.employee.employee import Employee, AmountBonus, PercentBonus
from ODP.employee.employee import Premium_employee


class TestEmployee:

    def test_init(self):
        e = Employee("Jan", "Nowak", 100)
        assert e.name == "Jan"
        assert e.last_name == "Nowak"
        assert e.rate_per_hour == 100

    def test_register_time(self):
        e = Employee("Jan", "Nowak", 100)
        e.register_time(5)
        assert e.registered_hours == 5

    def test_pay_salary_normal_hours(self):
        e = Employee("Jan", "Nowak", 100)
        e.register_time(5)
        assert e.pay_salary() == 500

    def test_pay_salary_with_no_registered_hours(self):
        e = Employee("Jan", "Nowak", 100)
        e.register_time(0)
        assert e.pay_salary() == 0

    def test_pay_salary_overhours(self):
        e = Employee("Jan", "Nowak", 100)
        e.register_time(10)
        assert e.pay_salary() == 1200

# test Premium_employee

    def test_init_premium_employee(self):
        e = Premium_employee("Jan", "Nowak", 100)
        assert e.name == "Jan"
        assert e.last_name == "Nowak"
        assert e.rate_per_hour == 100

    def test_register_time_premium_employee(self):
        e = Premium_employee("Jan", "Nowak", 100)
        e.register_time(5)
        assert e.registered_hours == 5

    def test_give_amount_bonus_to_premium_employee(self):
        e = Premium_employee("Jan", "Nowak", 100)
        self.bonus = AmountBonus(1000)
        e.give_bonus(self.bonus)
        assert e.bonuses == [self.bonus]

    def test_give_percent_bonus_to_premium_employee(self):
        e = Premium_employee("Jan", "Nowak", 100)
        self.bonus = PercentBonus(10)
        e.give_bonus(self.bonus)
        assert e.bonuses == [self.bonus]

    def test_pay_salary_normal_hours_plus_bonus(self):
        e = Employee("Jan", "Nowak", 100)
        e.register_time(5)
        e.give_bonus(1000)
        assert e.pay_salary() == 1500