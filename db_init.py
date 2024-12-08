import sqlite3

# Connect to SQLite database (creates the file if it doesn't exist)
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Create a table for storing user credentials
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password TEXT NOT NULL
)
''')

# Insert sample users (Run this once to add initial users)
cursor.execute("INSERT OR IGNORE INTO users (username, password) VALUES ('admin', 'admin123')")
cursor.execute("INSERT OR IGNORE INTO users (username, password) VALUES ('user1', 'password123')")

print("Database and users table created successfully!")

conn.commit()
conn.close()
