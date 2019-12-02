from employee import Employee

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