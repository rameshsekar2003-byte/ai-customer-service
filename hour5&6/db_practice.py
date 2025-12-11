import sqlite3
import time

# 1. Database Connect (Oru pudhu file create aagum)
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# 2. Table Clean-up (Pazhaya table irundha delete panniduvom for fresh start)
cursor.execute('DROP TABLE IF EXISTS users')
conn.commit()

# 3. Table Create
cursor.execute('''
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        username TEXT,
        email TEXT
    )
''')

# --- THE SECRET WEAPON (INDEX) ---
# Idhu irukkurathala dhaan search fast-a irukkum
# cursor.execute('CREATE INDEX idx_email ON users(email)')

# 4. Inserting 100,000 Dummy Users
print("100,000 Users generate aagitu iruku... Konjam wait pannunga...")

users_data = []
for i in range(100000):
    users_data.append((f"user{i}", f"user{i}@example.com"))

# Oreadiya insert pandrom (Bulk Insert)
cursor.executemany('INSERT INTO users (username, email) VALUES (?, ?)', users_data)
conn.commit()
print("Data Inserted Successfully! ✅")

# 5. Search Function (Time Measure Panna)
def search_user(email):
    print(f"\nSearching for {email}...")
    start_time = time.time()
    
    # Query run aaguthu
    cursor.execute('SELECT * FROM users WHERE email = ?', (email,))
    result = cursor.fetchone()
    
    end_time = time.time()
    
    if result:
        print(f"Found: {result}")
    else:
        print("Not Found")
        
    print(f"⏱️ Search Time: {end_time - start_time:.6f} seconds")

# Let's search for the LAST user (Worst case scenario)
search_user("user99999@example.com")

conn.close()