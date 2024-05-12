class Car:
    def __init__(self, make, model):
        self.public_make = make # Открытый атрибут
        self._protected_model = model # Защищенный атрибут
        self.__private = 2024 # Приватный атрибут
    def public_method(self):
        return f"Это открытый метод. Машина  {self.public_make} {self._protected_model}"
    def protected_method(self):
        return "Это защищенный метод"
    def __private_method(self):
        return "Это приватный метод"
class ElektricCar(Car):
    def __init__(self, make, model, battery_size):
        # Можно использовать super().__init__(make, model)
        super().__init__(make, model)
        # Нельзя использовать self.__private
        self.battery = battery_size
    def get_details(self):
        details = f"{self.public_make} {self._protected_model}, Бфтарея {self.battery} kWh"
        return details

tesla = ElektricCar("Tesla", "Model S", 100)
print(tesla.public_make)
print(tesla.public_method())

print(tesla._protected_model)
print(tesla._protected_method())

print(tesla._Car__private_year)



