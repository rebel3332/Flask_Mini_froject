class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        print(f'Зарегистрирован новый пользователь {self.name}')
