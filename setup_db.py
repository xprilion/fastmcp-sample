"""Database setup script."""

import database

if __name__ == "__main__":
    print("Initializing database...")
    database.init_database()
    print(f"Database initialized successfully at {database.DB_PATH}")

