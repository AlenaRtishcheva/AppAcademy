import sqlite3 as sq

class User:
    '''class for user with functions '''
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.migrate = Migrate()

    def get_groups(self):
        self.migrate.get_group()
        
    def get_tutors(self):
        #вставить миграчию функцию
        pass
    def get_departments(self):
        #вставить миграчию функцию
        pass

class Migrate:

    def get_group(self):
        try:
            with sq.connect() as db:
                cursor = db.cursor('Академия_65.db')
                cursor.execute('''SELECT группы.id, Группы.название, Группы.курс
                                  FROM Группы''')
                result = cursor.fetchall()
                for info in result:
                    line = str(info[0]) + '. ' + info[1] + ', курс: ' + str(info[2])
                    print (line)
        except:
            print ('Ошибка базы данных')

user = User('login', 'password')
user.get_groups()
