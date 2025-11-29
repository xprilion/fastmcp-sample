"""Database module for SQLite operations."""

import sqlite3
import os
from typing import List, Optional, Dict, Any
from datetime import datetime


DB_PATH = "todos.db"


def get_db_connection() -> sqlite3.Connection:
    """Get a database connection."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_database():
    """Initialize the database with the todos table."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS todos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            completed BOOLEAN DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    conn.commit()
    conn.close()


def create_todo(title: str, description: Optional[str] = None) -> Dict[str, Any]:
    """Create a new todo item."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        INSERT INTO todos (title, description)
        VALUES (?, ?)
    """, (title, description))
    
    todo_id = cursor.lastrowid
    conn.commit()
    
    cursor.execute("SELECT * FROM todos WHERE id = ?", (todo_id,))
    todo = dict(cursor.fetchone())
    conn.close()
    
    return todo


def get_all_todos(completed: Optional[bool] = None) -> List[Dict[str, Any]]:
    """Get all todos, optionally filtered by completion status."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    if completed is None:
        cursor.execute("SELECT * FROM todos ORDER BY created_at DESC")
    else:
        cursor.execute(
            "SELECT * FROM todos WHERE completed = ? ORDER BY created_at DESC",
            (1 if completed else 0,)
        )
    
    todos = [dict(row) for row in cursor.fetchall()]
    conn.close()
    
    return todos


def get_todo_by_id(todo_id: int) -> Optional[Dict[str, Any]]:
    """Get a todo by its ID."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM todos WHERE id = ?", (todo_id,))
    row = cursor.fetchone()
    conn.close()
    
    return dict(row) if row else None


def update_todo(
    todo_id: int,
    title: Optional[str] = None,
    description: Optional[str] = None,
    completed: Optional[bool] = None
) -> Optional[Dict[str, Any]]:
    """Update a todo item."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    updates = []
    params = []
    
    if title is not None:
        updates.append("title = ?")
        params.append(title)
    
    if description is not None:
        updates.append("description = ?")
        params.append(description)
    
    if completed is not None:
        updates.append("completed = ?")
        params.append(1 if completed else 0)
    
    if not updates:
        conn.close()
        return None
    
    updates.append("updated_at = CURRENT_TIMESTAMP")
    params.append(todo_id)
    
    cursor.execute(
        f"UPDATE todos SET {', '.join(updates)} WHERE id = ?",
        params
    )
    
    conn.commit()
    
    cursor.execute("SELECT * FROM todos WHERE id = ?", (todo_id,))
    row = cursor.fetchone()
    conn.close()
    
    return dict(row) if row else None


def delete_todo(todo_id: int) -> bool:
    """Delete a todo item."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM todos WHERE id = ?", (todo_id,))
    deleted = cursor.rowcount > 0
    
    conn.commit()
    conn.close()
    
    return deleted

