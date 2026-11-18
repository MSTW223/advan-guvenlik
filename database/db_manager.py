import sqlite3
import os
import bcrypt

# وضع قاعدة البيانات في مجلد آمن داخل مستندات المستخدم أو مسار البرنامج لضمان صلاحيات الكتابة
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_DIR = os.path.join(BASE_DIR, "database")

if not os.path.exists(DB_DIR):
    try:
        os.makedirs(DB_DIR, exist_ok=True)
    except Exception:
        DB_DIR = BASE_DIR  # في حال لم يتمكن، يحفظها في المجلد الرئيسي مباشرة

DB_PATH = os.path.join(DB_DIR, "advan_guvenlik.db")

class DatabaseManager:
    def __init__(self, db_path=DB_PATH):
        self.db_path = db_path
        self.init_database()

    def get_connection(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA foreign_keys = ON;")
        return conn

    def init_database(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS parking_locations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            address TEXT,
            capacity INTEGER NOT NULL DEFAULT 100,
            parking_type TEXT CHECK(parking_type IN ('paid', 'free')) NOT NULL DEFAULT 'paid',
            hourly_rate REAL DEFAULT 25.0,
            daily_rate REAL DEFAULT 0.0,
            free_initial_minutes INTEGER DEFAULT 15,
            max_daily_charge REAL DEFAULT 0.0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );""")

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            full_name TEXT,
            role TEXT CHECK(role IN ('Administrator', 'Manager', 'Operator', 'Viewer')) DEFAULT 'Operator',
            is_active BOOLEAN DEFAULT 1
        );""")

        cursor.execute("SELECT COUNT(*) FROM users;")
        if cursor.fetchone()[0] == 0:
            hashed_pw = bcrypt.hashpw("admin123".encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            cursor.execute("INSERT INTO users (username, password_hash, full_name, role) VALUES (?, ?, ?, ?)",
                           ("admin", hashed_pw, "System Administrator", "Administrator"))

        conn.commit()
        conn.close()
