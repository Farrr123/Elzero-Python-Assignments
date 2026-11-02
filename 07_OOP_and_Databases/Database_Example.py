"""SQLite database example: create, insert, retrieve, and delete users."""

import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "elzero.db"


def main() -> None:
    """Run the SQLite database example."""
    db = sqlite3.connect(DB_PATH)

    try:
        cursor = db.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id_user INTEGER PRIMARY KEY,
                name TEXT,
                email TEXT UNIQUE,
                birthdate DATE
            )
        """)

        users = [
            (1, "John Doe", "H6O8o@example.com", "1990-01-01"),
            (2, "Jane Smith", "bq8eE@example.com", "1995-02-02"),
            (3, "Bob Johnson", "t9YjI@example.com", "1980-03-03"),
            (4, "Alice Williams", "M4PZ2@example.com", "1998-04-04"),
        ]

        cursor.executemany(
            """
            INSERT OR IGNORE INTO users
            (id_user, name, email, birthdate)
            VALUES (?, ?, ?, ?)
            """,
            users,
        )

        db.commit()

        cursor.execute("SELECT * FROM users ORDER BY id_user DESC LIMIT 1")
        result = cursor.fetchone()

        print("Last User:", result)

        user_id = input("Please enter ID of the user to delete: ").strip()

        try:
            user_id = int(user_id)
        except ValueError:
            print("Please enter a valid numeric ID.")
            return

        cursor.execute(
            "SELECT * FROM users WHERE id_user = ?",
            (user_id,),
        )

        user = cursor.fetchone()

        if user:
            cursor.execute(
                "DELETE FROM users WHERE id_user = ?",
                (user_id,),
            )

            db.commit()

            print("User Deleted.")
            print("Show Other Data:")

            cursor.execute("SELECT * FROM users ORDER BY id_user ASC")

            for row in cursor.fetchall():
                print(
                    f"ID => {row[0]}, Name => {row[1]}, "
                    f"Date Of Birth => {row[3]}, Email => {row[2]}"
                )
        else:
            print("User Not Found.")

    finally:
        db.close()


if __name__ == "__main__":
    main()
