import sqlite3

# Connect to the database
conn = sqlite3.connect('travel_vibes.db')

# Create tables
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        phone TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS profiles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        place TEXT NOT NULL,
        district TEXT NOT NULL,
        state TEXT NOT NULL,
        description TEXT,
        next_trip_description TEXT,
        profile_image TEXT
    )
''')

# Save changes and close the connection
conn.commit()
conn.close()

print("Database and tables created successfully!")
