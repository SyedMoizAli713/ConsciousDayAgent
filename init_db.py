import sqlite3

conn = sqlite3.connect('entries.db')
c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS entries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    journal TEXT,
    intention TEXT,
    dream TEXT,
    priorities TEXT,
    reflection TEXT,
    strategy TEXT
)
''')

conn.commit()
conn.close()

print("Database initialized successfully.")
