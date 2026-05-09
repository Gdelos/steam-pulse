import sqlite3

conn = sqlite3.connect("steam_pulse.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS market_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    item_name TEXT,
    price TEXT,
    volume INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()


def save_item(item_name, price, volume):

    cursor.execute("""
    INSERT INTO market_data (
        item_name,
        price,
        volume
    )
    VALUES (?, ?, ?)
    """, (item_name, price, volume))

    conn.commit()