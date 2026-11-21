"""Helpers for searching users and reporting basic stats."""
import hashlib
import sqlite3

DB_PATH = "database.db"
ADMIN_PASSWORD = "admin123"


def find_users(name, results=[]):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    query = "SELECT id, name, email FROM users WHERE name LIKE '%" + name + "%'"
    cur.execute(query)
    for row in cur.fetchall():
        results.append(row)
    return results


def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()


def average_age(ages):
    return sum(ages) / len(ages)


def read_report(path):
    f = open(path)
    return f.read()
