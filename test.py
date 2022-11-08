# python todo.py --add "Wstaw ziemniaki"
# python todo.py --list
# python todo.py --toggle 1

import sqlite3
from argparse import ArgumentParser

parser = ArgumentParser(description='Mała aplikacja TODO')
parser.add_argument('--install', help='Instalacja! Uwaga, wyczyści bazę danych', action='store_true')
parser.add_argument('--add', help='Dodaj nowe zadanie')
parser.add_argument('--list', help='Wpisz tematy do zrobienia.', action='store_true')
parser.add_argument('--toggle', help='Zmień status zadania')
args = parser.parse_args()

connection = sqlite3.connect('todo.db')
cursor = connection.cursor()


if args.install:
    print('Instalujemy program')
    cursor.execute('DROP TABLE todos')
    cursor.execute('CREATE TABLE todos(id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, is_done BOOLEAN)')
    connection.commit

if args.add is not None:
    print('Dodajemy..')
    title = args.add
    cursor.execute('INSERT INTO todos(title, is_done) VALUES(?, false)', (title,))
    connection.commit()

if args.toggle is not None:
    print('Przełączamy...')

if args.list:
    print('Wyświetlamy')