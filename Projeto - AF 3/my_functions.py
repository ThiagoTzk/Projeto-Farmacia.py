import sqlite3
from decorators import connection_db

## -------------------------
## --------Functions--------

@connection_db
def register(cursor, username, password):
    sql = 'INSERT INTO users(username, password) VALUES(?, ?)'
    return cursor.execute(sql, [username, password])
    
@connection_db
def login(cursor, username, password):
    sql = 'SELECT * FROM users WHERE username = ? and password = ?'
    return cursor.execute(sql, [username, password]).fetchone()

@connection_db
def register_products(cursor, product_name, product_stripe, product_price, product_quantity):
    sql = 'INSERT INTO products(product_name, product_stripe, product_price, product_quantity) VALUES (?, ?, ?, ?)'
    return cursor.execute(sql, [product_name, product_stripe, product_price, product_quantity])
    
@connection_db
def list_products(cursor):
    sql = 'SELECT * FROM products'
    return cursor.execute(sql).fetchall()
    
@connection_db
def update_products(cursor, product_id, product_name, product_stripe, product_price, product_quantity):
    sql = 'UPDATE products SET product_name = ?, product_stripe = ?, product_price = ?, product_quantity = ? WHERE product_id = ?'
    return cursor.execute(sql, [product_name, product_stripe, product_price, product_quantity, product_id])
    
@connection_db
def remove_products(cursor, product_id):
    sql = 'DELETE FROM products WHERE product_id = ?'
    return cursor.execute(sql, [product_id])
    
@connection_db
def buy_products(cursor, product_id, product_quantity):
    sql = 'UPDATE products SET product_quantity = product_quantity - ? WHERE product_id = ?'
    return cursor.execute(sql, [product_quantity, product_id])

## -------------------------