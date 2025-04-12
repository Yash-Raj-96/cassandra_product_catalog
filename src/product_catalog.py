from cassandra.cluster import Cluster
import uuid

# Connect to Cassandra
cluster = Cluster(['127.0.0.1'])
session = cluster.connect('ecommerce')

# Insert sample product
def insert_product(name, price, category, stock):
    product_id = uuid.uuid4()
    session.execute("""
        INSERT INTO products (product_id, product_name, price, category, stock)
        VALUES (%s, %s, %s, %s, %s)
    """, (product_id, name, price, category, stock))
    print(f"Inserted product {name} with ID {product_id}")

# Fetch and display products
def fetch_products():
    rows = session.execute("SELECT * FROM products;")
    for row in rows:
        print(f"{row.product_name} | Price: {row.price} | Category: {row.category} | Stock: {row.stock}")

# Example usage
insert_product('MacBook Pro 16"', 240000.00, 'Laptop', 20)
fetch_products()
