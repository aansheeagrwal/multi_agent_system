import sqlite3
import os
from datetime import datetime

class MemoryStore:
    def __init__(self, db_path='memory_store.db'):
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS input_metadata (
                id TEXT PRIMARY KEY,
                source TEXT,
                timestamp TEXT,
                classification TEXT
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS extracted_fields (
                input_id TEXT,
                field_key TEXT,
                field_value TEXT,
                FOREIGN KEY (input_id) REFERENCES input_metadata(id)
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS action_traces (
                input_id TEXT,
                action TEXT,
                status TEXT,
                timestamp TEXT,
                FOREIGN KEY (input_id) REFERENCES input_metadata(id)
            )
        ''')
        self.conn.commit()

    def save_input_metadata(self, input_id, metadata):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT OR REPLACE INTO input_metadata (id, source, timestamp, classification)
            VALUES (?, ?, ?, ?)
        ''', (
            input_id,
            metadata.get("source", "unknown"),
            metadata.get("timestamp", datetime.now().isoformat()),
            metadata.get("classification", "unknown")
        ))
        self.conn.commit()

    def save_extracted_fields(self, input_id, fields):
        cursor = self.conn.cursor()
        for key, value in fields.items():
            cursor.execute('''
                INSERT INTO extracted_fields (input_id, field_key, field_value)
                VALUES (?, ?, ?)
            ''', (input_id, key, str(value)))
        self.conn.commit()

    def save_action_trace(self, input_id, action, status):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO action_traces (input_id, action, status, timestamp)
            VALUES (?, ?, ?, ?)
        ''', (input_id, action, status, datetime.now().isoformat()))
        self.conn.commit()

    def get_input_metadata(self, input_id):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM input_metadata WHERE id=?', (input_id,))
        return cursor.fetchone()

    def get_all_traces(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM action_traces')
        return cursor.fetchall()

    def close(self):
        self.conn.close()
