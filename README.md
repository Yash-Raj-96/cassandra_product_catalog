# 🛒 NoSQL Database for E-Commerce – Cassandra Product Catalog

This project demonstrates how to set up a simple e-commerce product catalog using **Apache Cassandra**, a distributed NoSQL database. It showcases how NoSQL databases efficiently handle large-scale data, which is crucial for applications like e-commerce.

---

## 📌 Project Overview

This mini-project includes:

- Creating a **keyspace** for an e-commerce application.
- Defining a **product table** to hold catalog data.
- Performing **CRUD** operations: Insert, Select, Update, and Delete.
- Executing basic CQL (Cassandra Query Language) queries in `cqlsh`.

---

## 🧾 Dataset Details

- **Dataset Name**: E-commerce Product Catalog (Manual Entry)
- **Size**: Less than 10 KB
- **Attributes**:
  - `product_id` (UUID)
  - `product_name` (text)
  - `price` (decimal)
  - `category` (text)
  - `stock` (int)

---

## ⚙️ Setup Instructions

1. **Install Apache Cassandra** on your system.
2. Start the Cassandra server:
   ```bash
   cassandra -f
   ```
3. Open the CQL shell:
   ```bash
   cqlsh
   ```
4. Run the queries provided below to create the keyspace and table.

---

## 🧑‍💻 Important Code Snippets

### ✅ Create Keyspace
```sql
CREATE KEYSPACE ecommerce
WITH replication = {'class':'SimpleStrategy', 'replication_factor' : 1};
```

### ✅ Create Product Table
```sql
CREATE TABLE products (
    product_id UUID PRIMARY KEY,
    product_name text,
    price decimal,
    category text,
    stock int
);
```

### ✅ Insert Product Records
```sql
INSERT INTO products (product_id, product_name, price, category, stock)
VALUES (uuid(), 'iPhone 14', 79999.00, 'Smartphone', 50);
```

### ✅ View All Products
```sql
SELECT * FROM products;
```

### ✅ Update Stock
```sql
UPDATE products SET stock = 45 WHERE product_id = <your_product_uuid>;
```

### ✅ Delete a Product
```sql
DELETE FROM products WHERE product_id = <your_product_uuid>;
```

## ✅ Expected Output

- A functional Cassandra product catalog database.
- Ability to insert, view, update, and delete product records.
- Query results displayed within the `cqlsh` shell.

---

## 📚 References

- [Apache Cassandra Documentation](https://cassandra.apache.org/doc/)
- [CQL Language Reference](https://cassandra.apache.org/doc/latest/cql/)

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
