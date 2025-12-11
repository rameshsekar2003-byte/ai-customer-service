import sqlite3

# 1. Database & Admin Setup
conn = sqlite3.connect('vulnerable.db')
cursor = conn.cursor()

# Admin Account Create Pandrom
cursor.execute('DROP TABLE IF EXISTS users')
cursor.execute('CREATE TABLE users (username TEXT, password TEXT)')
cursor.execute("INSERT INTO users VALUES ('admin', 'MyC0mpl3xP@ssw0rd')")
conn.commit()

print("--- 🕵️ SECURE LOGIN SYSTEM (Fixed) ---")

def login():
    username = input("Enter username: ")
    password = input("Enter password: ") 

    # ✅ THE FIX: Placeholders (?) use pandrom
    # Ippo SQL Injection vela seyyadhu!
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    
    # Python kitta solrom: "Indha Query-a run pannu, indha data-va (?) ulla fill pannikko"
    cursor.execute(query, (username, password))
    
    user = cursor.fetchone()
    
    if user:
        print("✅ Login Successful! Welcome Admin!")
    else:
        print("❌ Login Failed! (Security Fix Worked)")

# --- MUKKIYAMANA LINE (Ithai than naan miss panniten!) ---
login()
conn.close()