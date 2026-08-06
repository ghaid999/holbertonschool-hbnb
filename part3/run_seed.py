#!/usr/bin/env python3
"""Creates the SQLite database tables and seeds initial data.

Schema + amenities come from the raw SQL files.
The admin user is created through the Flask app itself (using its own
bcrypt config via User.hash_password) instead of a hardcoded hash,
so the password always matches correctly no matter who runs this script.

IMPORTANT: sql_scripts/2_initial_data.sql must NOT contain the admin
INSERT anymore (remove that block) - only the amenities INSERTs should
remain there. The admin is created below in Python instead.
"""
import sqlite3

DB_PATH = "hbnb.db"
SQL_FILES = [
    "sql_scripts/1_schema.sql",
    "sql_scripts/2_initial_data.sql",   # amenities only (admin block removed)
]

conn = sqlite3.connect(DB_PATH)
for sql_file in SQL_FILES:
    print(f"Running {sql_file} ...")
    with open(sql_file, "r") as f:
        conn.executescript(f.read())
    print("  -> done")
conn.commit()
conn.close()

# Create the admin user through the actual Flask app + bcrypt config
from app import create_app, db
from app.models.user import User

app = create_app()
with app.app_context():
    admin = User.query.filter_by(email="admin@hbnb.io").first()
    if not admin:
        admin = User(
            id="36c9050e-ddd3-4c3b-9731-9f487208bbc1",
            first_name="Admin",
            last_name="HBnB",
            email="admin@hbnb.io",
            is_admin=True,
        )
        admin.hash_password("admin1234")
        db.session.add(admin)
    else:
        admin.is_admin = True
        admin.hash_password("admin1234")
    db.session.commit()
    print("Admin user created/updated with a correctly matching password hash.")

print("All done. Database seeded successfully.")