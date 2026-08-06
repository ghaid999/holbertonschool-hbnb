#!/usr/bin/env python3
"""Creates the SQLite database tables and seeds initial data."""
import sqlite3

DB_PATH = "hbnb.db"

# Run in order: schema first, then data, then (optionally) the test script
SQL_FILES = [
    "sql_scripts/1_schema.sql",
    "sql_scripts/2_initial_data.sql",
    # "3_crud_test.sql",   # uncomment only if you want to run the test/demo queries too
]

conn = sqlite3.connect(DB_PATH)

for sql_file in SQL_FILES:
    print(f"Running {sql_file} ...")
    with open(sql_file, "r") as f:
        script = f.read()
    conn.executescript(script)
    print(f"  -> done")

conn.commit()
conn.close()

print("All done. Database seeded successfully.")