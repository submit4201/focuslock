import sqlite3
from focuslock.models.reminder import Reminder
from focuslock.models.task import Task
from focuslock.models.lockstate import LockState

class Database:
    def __init__(self, db_path='focuslock.db'):
        self.db_path = db_path
        self.conn = None

    def connect(self):
        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS reminders (
                id TEXT PRIMARY KEY,
                title TEXT,
                description TEXT,
                due_time TEXT,
                lock_enabled BOOLEAN,
                whitelist TEXT,
                task_id TEXT,
                completed BOOLEAN
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id TEXT PRIMARY KEY,
                title TEXT,
                type TEXT,
                requirement TEXT,
                fulfilled BOOLEAN,
                notes TEXT
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS lockstates (
                id TEXT PRIMARY KEY,
                active BOOLEAN,
                start_time TEXT,
                forced_end_time TEXT,
                task_id TEXT,
                override_used BOOLEAN
            )
        ''')
        self.conn.commit()

    def save_reminder(self, reminder: Reminder):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT OR REPLACE INTO reminders (id, title, description, due_time, lock_enabled, whitelist, task_id, completed)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (reminder.id, reminder.title, reminder.description, reminder.due_time.isoformat(), reminder.lock_enabled, ','.join(reminder.whitelist), reminder.task_id, reminder.completed))
        self.conn.commit()

    def get_reminder(self, reminder_id: str) -> Reminder:
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM reminders WHERE id = ?', (reminder_id,))
        row = cursor.fetchone()
        return Reminder.from_dict(dict(row)) if row else None

    def get_all_reminders(self) -> list[Reminder]:
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM reminders')
        rows = cursor.fetchall()
        return [Reminder.from_dict(dict(row)) for row in rows]

    def save_task(self, task: Task):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT OR REPLACE INTO tasks (id, title, type, requirement, fulfilled, notes)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (task.id, task.title, task.type, task.requirement, task.fulfilled, task.notes))
        self.conn.commit()

    def get_task(self, task_id: str) -> Task:
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM tasks WHERE id = ?', (task_id,))
        row = cursor.fetchone()
        return Task.from_dict(dict(row)) if row else None

    def save_lockstate(self, lockstate: LockState):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT OR REPLACE INTO lockstates (id, active, start_time, forced_end_time, task_id, override_used)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (lockstate.id, lockstate.active, lockstate.start_time.isoformat(), lockstate.forced_end_time.isoformat(), lockstate.task_id, lockstate.override_used))
        self.conn.commit()

    def get_lockstate(self, lockstate_id: str) -> LockState:
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM lockstates WHERE id = ?', (lockstate_id,))
        row = cursor.fetchone()
        return LockState.from_dict(dict(row)) if row else None

    def get_active_lockstate(self) -> LockState:
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM lockstates WHERE active = ?', (True,))
        row = cursor.fetchone()
        return LockState.from_dict(dict(row)) if row else None


    def close(self):
        if self.conn:
            self.conn.close()
