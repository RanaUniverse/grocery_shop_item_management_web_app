<!-- here i will keep how the database will works and the database's structer and so on.
The database idea will be written here. -->

# Database Design
It will be `products` & `category`.

## How to use SQLITE DATABASE?
For sqlite i dont need to do anything special, in the create_engine() function i need to give teh path of the database name only.

## How to use POSTGRES?
For postgres i need to start the service first and then come to use this.
suppose database name is: `grocery_db`
So in this case first i need to make sure this is exists and postgres is running.
```
sudo systemctl status postgresql
```
If it say not started or inactive then i need to run this service first with below command:
```
sudo systemctl start postgresql
```
If i dont start this service it will shows the connection refused.

### How about making a database in the postgres?
```terminal
rana@laptop:~$ sudo -iu postgres
[sudo] password for rana: 
postgres@laptop:~$ psql
psql (18.3 (Ubuntu 18.3-1.pgdg24.04+1))
Type "help" for help.

postgres=# 
postgres=# 
postgres=# create database laptop_data owner rana;
CREATE DATABASE
postgres=# 
```



# 🗄️ Database Design

## 📦 Products Table

- id_
- name
- category_id
- buy_price
- sell_price
- mrp
- discount_percent
- stock_quantity
- updated_at -> i will store the posix int value here

---

## 📂 Categories Table

- id
- name

---

## 🔗 Relationships

- One category → many products