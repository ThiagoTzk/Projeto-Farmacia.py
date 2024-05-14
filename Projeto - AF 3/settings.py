import sqlite3

conn = sqlite3.connect('db.sqlite')

cursor = conn.cursor()

## ---------------------------
## -----[Creating Tables]-----

## [Users Table]
sql = '''CREATE TABLE IF NOT EXISTS users(

id INTEGER PRIMARY KEY AUTOINCREMENT,
username varchar(255),
password varchar(255)
)'''

cursor.execute(sql)

## [Products Table]
sql = '''CREATE TABLE IF NOT EXISTS products(

product_id INTEGER PRIMARY KEY AUTOINCREMENT,
product_name varchar(255),
product_stripe varchar(255),
product_price float,
product_quantity INTEGER
)'''

cursor.execute(sql)

## -------------------------------
## ---[Predefined Informations]---

## [Admin Account]
sql = 'INSERT INTO users(username, password) VALUES(?, ?)'
cursor.execute(sql, ['4Disease', 'admin'])
conn.commit()

## [Products]
sql = 'INSERT INTO products(product_name, product_stripe, product_price, product_quantity) VALUES(?, ?, ?, ?)'
cursor.execute(sql, ['Dorflex', 'No-Stripe', 11.90, 20])
conn.commit()

sql = 'INSERT INTO products(product_name, product_stripe, product_price, product_quantity) VALUES(?, ?, ?, ?)'
cursor.execute(sql, ['Paracetamol', 'Yellow', 7.90, 30])
conn.commit()

sql = 'INSERT INTO products(product_name, product_stripe, product_price, product_quantity) VALUES(?, ?, ?, ?)'
cursor.execute(sql, ['Loratamed', 'No-Stripe', 5.90, 15])
conn.commit()

## -------------------------------