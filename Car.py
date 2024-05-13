class Car:
    def __init__(self, make, model):
        self.public_make = make # Открытый атрибут
        self._protected_model = model # Защищенный атрибут
        self.__private_year = 2024 # Приватный атрибут
    def public_method(self):
        return f"Это открытый метод. Машина: {self.public_make} {self._protected_model}."
    def _protected_method(self):
        return "Это защищенный метод"
    def __private_method(self):
        return "Это приватный метод"
class ElektricCar(Car):
    def __init__(self, make, model, battery_size):
        # Можно использовать super().__init__(make, model)
        super().__init__(make, model)
        # Нельзя использовать self.__private
        self.battery_size = battery_size
    def get_details(self):
        # Можно обратиться к открытому и защищенномуатрибуту, но не к приватному
        details = f"{self.public_make} {self._protected_model}, Батарея: {self.battery} kWh."
        # Нельзя обратиться к __private_method и __private_year
        return details
# Создание экземпляра
tesla = ElektricCar("Tesla", "Model S", 100)
# Доступ к открытому атрибуту и методу:
print(tesla.public_make)
print(tesla.public_method())
# Доступ к защищенному атрибуту и методу:
print(tesla._protected_model)
print(tesla._protected_method())
# Доступ к приватному атрибуту и методу напрямую не возможен, но Python позволяет обойти приватность и обратиться к нему по имени:
print(tesla._Car__private_year) # Доступ к приватному атрибуту по имени (через _Car(название класса) Mandlinq



