# lib/config.py
import sqlite3

conn = sqlite3.connect('company.db')
cursor = conn.cursor()
