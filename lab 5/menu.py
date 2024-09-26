import sqlite3 

db = 'records.db'
"""
A menu - you need to add the database and fill in the functions. 
"""

# TODO create database table OR set up Peewee model to create table

def create_table():
    with sqlite3.connect(db) as conn:
        conn.execute ('CREATE TABLE IF NOT EXISTS records')
    conn.close()


def main():
    menu_text = """
    1. Display all records
    2. Search by name
    3. Add new record
    4. Edit existing record
    5. Delete record 
    6. Quit
    """

    while True:
        print(menu_text)
        choice = input('Enter your choice: ')
        if choice == '1':
            display_all_records()
        elif choice == '2':
            search_by_name()
        elif choice == '3':
            add_new_record()
        elif choice == '4':
            edit_existing_record()
        elif choice == '5':
            delete_record()
        elif choice == '6':
            break
        else:
            print('Not a valid selection, please try again')


def display_all_records():
    conn = sqlite3.connect(db)
    results = conn.execute('SELECT * FROM records')
    print('todo display all records')
    for row in results:
        print(row) 

    conn.close()


def search_by_name():
    name = input('Enter the name to search for: ')
    conn = sqlite3.connect(db)
    results = conn.execute('SELECT * FROM records WHERE name like ?')
    first_row = results.fetchone()
    if first_row:
        print('Your name is: ', first_row) 
    else:
        print('not found')
    conn.close()

    print('todo ask user for a name, and print the matching record if found. What should the program do if the name is not found?')


def add_new_record():
    name = input("Enter the name of the new record holder: ")
    catches = int(input("Enter the number of catches: "))

    with sqlite3.connect(db) as conn:
      conn.execute('INSERT INTO record_holder (name,catches) VALUES (?,?)', (name,catches))

      conn.close()

    print('todo add new record. What if user wants to add a record that already exists?')


def edit_existing_record():
    with sqlite3.connect(db) as conn:
        conn.execute('SELECT * FROM records WHERE name = ?')
        

    print('todo edit existing record. What if user wants to edit record that does not exist?') 


def delete_record(name):
    with sqlite3.connect(db) as conn:
        conn.execute('DELETE from RECORDS WHERE name = ?', (name, ))
    conn.close()

    print('todo delete existing record. What if user wants to delete record that does not exist?') 


if __name__ == '__main__':
    main()