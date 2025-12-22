Prompt:
Design an efficient database structure for e-commerce website

Design:
users -> make transactions on various products in the ecommerce site

users table
id, name, email, transactions

transactions table
id, product_id, amount, timestamp, payment (3rd party)

products table
id, name, cost, description

