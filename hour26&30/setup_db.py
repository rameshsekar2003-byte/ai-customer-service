import sqlite3

def setup_database():
    # 1. Connect to database (Idhu file-a create pannidum)
    conn = sqlite3.connect('orders.db')
    cursor = conn.cursor()

    # 2. Table Clean-up (Pazhaya table irundha delete panniduvom)
    cursor.execute('DROP TABLE IF EXISTS orders')

    # 3. Create 'orders' table
    cursor.execute('''
        CREATE TABLE orders (
            order_id TEXT PRIMARY KEY,
            customer_id TEXT,
            status TEXT,
            delivery_date TEXT
        )
    ''')

    # 4. Insert Dummy Data (5-10 orders)
    orders_data = [
        ('ORD-101', 'CUST-001', 'Shipped', '2025-10-25'),
        ('ORD-102', 'CUST-002', 'Pending', '2025-10-28'),
        ('ORD-103', 'CUST-001', 'Delivered', '2025-10-20'),
        ('ORD-104', 'CUST-003', 'Processing', '2025-10-27'),
        ('ORD-105', 'CUST-004', 'Cancelled', '2025-10-22'),
        ('ORD-106', 'CUST-002', 'Delivered', '2025-10-15'),
        ('ORD-107', 'CUST-005', 'Shipped', '2025-10-26')
    ]

    cursor.executemany('INSERT INTO orders VALUES (?, ?, ?, ?)', orders_data)
    conn.commit()
    
    print(f"Success! 'orders.db' created with {len(orders_data)} orders. ✅")
    conn.close()

if __name__ == "__main__":
    setup_database()