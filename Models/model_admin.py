class Admin:
    def __init__(self, login, password):
        self.login = login
        self.password = password

    def add_student(self):
        name = input('Введите имя студента: ')
        surname = input('Введите фамилию студента: ')
        reting = int(input('Введите рейтинг студента от 0 до 5: '))
        # Метод из миграции

    def add_teacher(self):
        isprofessor = int(input('Введите является ли преподаватель профессором или нет (0 или 1 соответственно): '))
        name = input('Введите имя преподавателя: ')
        surname = input('Введите фамилию преподаваетля: ')
        salary = input('Введите ставку преподавателя в рублях от 30000 до 70000): ')
        # Метод из миграции
'''
    def change_student(self):
        name = input('Введите имя студента: ')
        surname = input('Введите фамилию студента: ')
        reting = input('Введите рейтинг студента от 0 до 5: ')
        # Метод из миграции

    def change_teacher(self):
        isprofessor = int(input('Введите является ли преподаватель профессором или нет (0 или 1 соотвественно): '))
        name = input('Введите имя преподавателя: ')
        surname = input('Введите фамилию преподаваетля: ')
        reting = input('Введите рейтинг студента от 0 до 5: ')
        salary = input('Введите ставку преподавателя в рублях от 30000 до 70000): ')
        # Метод из миграции
        
    def delete_student(self):
        name = input('Введите имя студента: ')
        surname = input('Введите фамилию студента: ')
        reting = input('Введите рейтинг студента от 0 до 5: ')
        # Метод из миграции

    def delete_teacher(self):
        isprofessor = int(input('Введите является ли преподаватель профессором или нет (0 или 1 соотвественно): '))
        name = input('Введите имя преподавателя: ')
        surname = input('Введите фамилию преподаваетля: ')
        reting = input('Введите рейтинг студента от 0 до 5: ')
        salary = input('Введите ставку преподавателя в рублях от 30000 до 70000): ')
        # Метод из миграции
                          
''' 
        
