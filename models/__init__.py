# lib/config.py
import sqlite3

conn = sqlite3.connect('./database/magazine.db')
cursor = conn.cursor()
