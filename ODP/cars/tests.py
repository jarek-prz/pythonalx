from car import ElectricCar

class TestElectricCar:

    def test_init(self):
        c= ElectricCar(100)
        assert c.range()==100

    def test_drive_70(self):
        c = ElectricCar(100)
        assert c.drive(70)==70

    def test_drive_charge(self):
        c = ElectricCar(100)
        assert c.range() == 100
        assert c.drive(70) ==70
        assert c.drive(50) == 30
        assert c.drive(30) == 0
        c.charge()
        assert c.range() == 100


