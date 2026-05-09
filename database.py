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


def get_average_volume(item_name):

    cursor.execute("""
    SELECT AVG(volume)
    FROM market_data
    WHERE item_name = ?
    """, (item_name,))

    result = cursor.fetchone()

    if result[0]:
        return int(result[0])

    return 0

    def get_record_count(item_name):

    cursor.execute("""
    SELECT COUNT(*)
    FROM market_data
    WHERE item_name = ?
    """, (item_name,))

    result = cursor.fetchone()

    return result[0]