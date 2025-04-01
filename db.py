import sqlite3

DB_PATH = "status.db"

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS bot_status (
                id INTEGER PRIMARY KEY,
                active INTEGER NOT NULL
            );
        """)
        conn.execute("INSERT OR IGNORE INTO bot_status (id, active) VALUES (1, 0);")

def set_status(active: bool):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("UPDATE bot_status SET active = ? WHERE id = 1;", (1 if active else 0,))

def get_status() -> bool:
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.execute("SELECT active FROM bot_status WHERE id = 1;")
        result = cur.fetchone()
        return result[0] == 1 if result else False