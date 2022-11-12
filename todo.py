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
    query = cursor.execute('SELECT is_done FROM todos WHERE id=?', (args.toggle,))
    is_done = query.fetchone()
    if is_done is None:
        print('Nie mam takiego todo')
        quit()
    elif is_done[0] == 1:
        print('Zamieniam na niezrobione.')
        new_is_done = 0
    elif is_done[0] == 0:
        print('Zamieniam na zrobione')
        new_is_done = 1

    cursor.execute('UPDATE todos SET is_done=? WHERE id=?', (new_is_done, args.toggle))
    connection.commit()

if args.list:
    for todo_id, title, is_done in cursor.execute('SELECT id, title, is_done FROM todos'):
        print(f'{todo_id} \t {title} \t {"[v]" if is_done else "[ ]"}' )