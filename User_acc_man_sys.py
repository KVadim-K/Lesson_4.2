#Разработай систему управления учетными записями пользователей для небольшой компании. Компания разделяет сотрудников на обычных
# работников и администраторов. У каждого сотрудника есть уникальный идентификатор (ID), имя и уровень доступа. Администраторы, помимо
# обычных данных пользователей, имеют дополнительный уровень доступа и могут добавлять или удалять пользователя из системы.
# Требования:
# 1.Класс `User*: Этот класс должен инкапсулировать данные о пользователе: ID, имя и уровень доступа ('user' для обычных сотрудников).
# 2.Класс `Admin`: Этот класс должен наследоваться от класса `User`. Добавь дополнительный атрибут уровня доступа, специфичный для
# администраторов ('admin'). Класс должен также содержать методы `add_user` и `remove_user`,
# которые позволяют добавлять и удалять пользователей из списка (представь, что это просто список экземпляров `User`).
# 3.Инкапсуляция данных: Убедись, что атрибуты классов защищены от прямого доступа и модификации снаружи. Предоставь доступ к
# необходимым атрибутам через методы (например, get и set методы).

class User:
    def __init__(self, ID, name, access_level='user'):
        self.__private_ID = ID
        self.__private_name = name
        self.__private_access_level = access_level

    def get_ID(self):
        return self.__private_ID

    def set_ID(self, value):
        self.__private_ID = value

    def get_name(self):
        return self.__private_name

    def set_name(self, value):
        self.__private_name = value

    def get_access_level(self):
        return self.__private_access_level

    def set_access_level(self, value):
        self.__private_access_level = value

    ID = property(get_ID, set_ID)
    name = property(get_name, set_name)
    access_level = property(get_access_level, set_access_level)


class Admin(User):
    def __init__(self, ID, name):
        super().__init__(ID, name, access_level='admin')
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def remove_user(self, user):
        self.users.remove(user)


# Создание объектов пользователя и администратора
user = User(1, 'Иван')
admin = Admin(2, 'Пётр')

# Добавление и удаление пользователя администратором
admin.add_user(user)
admin.remove_user(user)

# Вывод данных через свойства
print("User ID:", user.ID)
print("User Name:", user.name)
print("User Access Level:", user.access_level)

print("Admin ID:", admin.ID)
print("Admin Name:", admin.name)
print("Admin Access Level:", admin.access_level)
