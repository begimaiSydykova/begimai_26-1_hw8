import sqlite3


def create_connection(db_name):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
        return conn
    except sqlite3.Error as e:
        print(e)


def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)


def create_products(conn, product):
    try:
        sql = '''INSERT INTO products 
        (product_title, price, quantity) 
        VALUES (?, ?, ?)
        '''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def update_quantity(conn, product):
    try:
        sql = '''UPDATE products SET quantity = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def update_price(conn, product):
    try:
        sql = '''UPDATE products SET price = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def delete_product(conn, id):
    try:
        sql = '''DELETE FROM products WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def select_all_products(conn):
    try:
        sql = '''SELECT * FROM products'''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()

        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)

def select_by_price(conn, limit):
    try:
        sql = '''SELECT * FROM products WHERE price <= ? AND quantity > 5'''
        cursor = conn.cursor()
        cursor.execute(sql, (limit,))
        rows = cursor.fetchall()

        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)


def select_by_product_title(conn):
    try:
        sql = '''SELECT * FROM products WHERE product_title LIKE 'I_h%' '''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()

        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)


database = r'hw.db'
sql_create_products_table = '''
CREATE TABLE products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR(200) NOT NULL,
price DOUBLE(10, 2) NOT NULL DEFAULT 0.0,
quantity DOUBLE(5, 0) NOT NULL DEFAULT 0
)
'''
connection = create_connection(database)
if connection is not None:
    print('Connected successfully')
    # create_table(connection, sql_create_products_table)
    # create_products(connection, ('Iphone 14 Pro Max', 1500.00, 20))
    # create_products(connection, ('Apple MacBook Pro 16-inch', 2745.21, 42))
    # create_products(connection, ('Apple MacBook Air 13-inch', 1654.09, 4))
    # create_products(connection, ('Midi JBL PartyBox 710', 951.71, 523))
    # create_products(connection, ('Apple AirPods Max', 626.71, 245))
    # create_products(connection, ('Apple EarPods Plug 3.5', 28.90, 2000))
    # create_products(connection, ('Apple iPad Pro 12.9 (5th Gen)', 1276.73, 40))
    # create_products(connection, ('Iphone 13 Pro Max', 1100.00, 15))
    # create_products(connection, ('Iphone 13 Pro', 900.00, 10))
    # create_products(connection, ('Iphone 14 Pro', 1300.00, 250))
    # create_products(connection, ('Apple iPad Pro 11', 928.50, 7))
    # create_products(connection, ('Apple iPad Air (10.9 Gen 4 2020)', 638.42, 320))
    # create_products(connection, ('Apple MacBook Pro 13 M2 (8C CPU/10C GPU)', 1857.11, 5))
    # create_products(connection, ('Apple MacBook Pro 16" M1 Pro 10-CPU 16-GPU 32UM 1 TB', 3482.30, 0))
    # create_products(connection, ('Mac mini, Apple M1, 8 ГБ, 256 ГБ SSD, 2020', 870.57, 11000))
    # update_quantity(connection, (50, 6))
    # select_by_price(connection, 100)
    select_all_products(connection)
    delete_product(connection, 2)
    # select_by_product_title(connection)
    connection.close
    print('Done')
