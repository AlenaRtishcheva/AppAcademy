import sqlite3 as sq

class Menu:
    def __init__(self):
        self.migrate = Migrate()
    
    def main(self):
        choice = None
        while choice != '0':
            print (
                '''\nМеню:
                    0 - Выйти
                    1 - Администратор
                    2 - Пользователь
                '''
                )   
        
            choice = input('Ваш выбор: ')
        
            if choice == '0':
                print ('Выход из меню!')
                
            elif choice == '1':
                self.log.create_basket_log()
        
            elif choice == '2':
                self.log.stastic_log()
   
            else:
                print ('Этот выбор не предусмотрен в меню!')


        
        while True:
            value = input(f'ПОИСК:\n1 - трек\n2 - исполнитель\n3 - альбом\n4 - представление\n5 - вывод всей информации\n6 - альбомы Битлз\n0 - выход')
            match value:
                case('1'):
                    track = input('Введите название трека:')
                    self.migrate.get_track(track)
                case('2'):
                    artist = input('Введите имя исполнителя:')
                    self.migrate.get_artist(artist)
                case('3'):
                    album = input('Введите название альбома:')
                    self.migrate.get_album(album)
                case('4'):
                    self.migrate.get_all_artist()
                case('5'):
                    self.migrate.get_full_info_track()
                case('6'):
                    self.migrate.get_album_beatles()
                case('0'):
                    print ('выход')
class Migrate:
    def __init__(self):
        self.path = 'Music.db'

    def get_track(self, name_track):
        try:
            with sq.connect('Music.db') as db:
                cursor = db.cursor()
                cursor.execute('''
                    SELECT track.name, artist.name FROM track, artist
                    WHERE track.name = ?
                    AND track.artist_id = artist.id 
                    GROUP BY artist.name
                ''', (name_track,))
                data = cursor.fetchall()
                if data:
                    print ('Результат поиска:')
                    for track in data:
                        print (f'Трек: {track[0]} - {track[1]}')
                else:
                    print ('По запросу ничего не найдено')
        except:
            print ('Ошибка базы данных')

    def get_artist(self, name_artist):
        try:
            with sq.connect('Music.db') as db:
                cursor = db.cursor()
                cursor.execute('''
                    SELECT track.name, artist.name
                    FROM track
                    JOIN artist ON artist.id = track.artist_id
                    WHERE artist.name = ?
                ''', (name_artist,))
                data = cursor.fetchall()
                if data:
                    print ('Результат поиска:')
                    for info in data:
                        print (f'Трек: {info[0]}')
                else:
                    print ('По запросу ничего не найдено')
        except:
            print ('Ошибка базы данных')
        
    def get_album(self, name_album):
        try:
            with sq.connect('Music.db') as db:
                cursor = db.cursor()
                cursor.execute('''
                    SELECT album.name, album.date, artist.name 
                    FROM album
                    JOIN artist ON album.artist_id = artist.id
                    WHERE album.name = ?
                ''', (name_album,))
                data = cursor.fetchall()
                if data:
                    print ('Результат поиска:')
                    for info in data:
                        print (f'Дата: {info[1]}, Артист: {info[2]}')
                else:
                    print ('По запросу ничего не найдено')
        except:
            print ('Ошибка базы данных')

    def get_all_artist(self):
        try:
            with sq.connect('Music.db') as db:
                cursor = db.cursor()
                cursor.execute('''
                    SELECT *
                    FROM all_artists
                ''')
                data = cursor.fetchall()
                if data:
                    print ('Результат поиска:')
                    for artist in data:
                        print (artist[0])
                else:
                    print ('По запросу ничего не найдено')
        except:
            print ('Ошибка базы данных')
            
    def get_full_info_track(self):
        try:
            with sq.connect('Music.db') as db:
                cursor = db.cursor()
                cursor.execute('''
                    SELECT *
                    FROM full_info_track
                ''')
                data = cursor.fetchall()
                if data:
                    print ('Результат поиска:')
                    for track in data:
                        print (track[0], track[1], track[2], track[3])
                else:
                    print ('По запросу ничего не найдено')
        except:
            print ('Ошибка базы данных')
        
    def get_album_beatles(self):
        try:
            with sq.connect('Music.db') as db:
                cursor = db.cursor()
                cursor.execute('''
                    SELECT *
                    FROM album_beatles
                ''')
                data = cursor.fetchall()
                if data:
                    print ('Результат поиска:')
                    for info in data:
                        print (info[0], info[1])
                else:
                    print ('По запросу ничего не найдено')
        except:
            print ('Ошибка базы данных')
            
menu = Menu()
menu.main()
          
 
        
