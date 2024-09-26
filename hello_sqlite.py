import sqlite3

db = 'first_db.sqlite'

def create_table():
    with sqlite3.connect(db) as conn:
         conn.execute ('CREATE TABLE IF NOT EXISTS products (id int, name text)')
    conn.close()

def insert_example_data():
    with sqlite3.connect(db) as conn:
         conn.execute ('INSERT INTO products values (1000, "hat")')
         conn.execute ('INSERT INTO products values (1001, "jacket")')
    conn.close()

def display_all_data():
    conn = sqlite3.connect(db)
    results = conn.execute('SELECT * FROM products')
    print('All product:')
    for row in results:
        print(row) #Each row is a tuple object.

    conn.close()

def display_one_product(product_name):

    conn = sqlite3.connect(db)
    results = conn.execute('SELECT * FROM products WHERE name like ?', (product_name,))
    first_row = results.fetchone()
    if first_row:
        print('Your prodcut is: ', first_row) 
    else:
        print('not found')
    conn.close()

def create_new_product():

    new_id = int(input('enter new id: '))
    new_name = input('enter new product name: ')

    with sqlite3.connect(db) as conn:
        conn.execute(f'INSERT INTO products VALUES (?,?)', (new_id, new_name))

    conn.close()

def update_product():
    updated_product = 'wool hat'
    update_id = 1000

    with sqlite3.connect(db) as conn:
        conn.execute('UPDATE products SET name = ? WHERE id = ? ', (updated_product, update_id) )

    conn.close()

def delete_product(product_name):
    with sqlite3.connect(db) as conn:
        conn.execute('DELETE from PRODUCTS WHERE name = ?', (product_name, ))
    conn.close()

create_table()
insert_example_data()
display_all_data()
display_one_product('jacket')
display_one_product('coat')
create_new_product()
update_product()
delete_product('jacket')
display_all_data()

