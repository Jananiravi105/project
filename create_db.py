import sqlite3

conn = sqlite3.connect("ebooks.db")
cursor = conn.cursor()

# Create tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    author TEXT,
    language TEXT,
    description TEXT,
    file_path TEXT
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS tags (
    tag_id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id INTEGER,
    tag TEXT,
    FOREIGN KEY (book_id) REFERENCES books(book_id)
)
""")

# Insert sample data
cursor.executemany("""
INSERT INTO books (title, author, language, description, file_path)
VALUES (?, ?, ?, ?, ?)
""", [
    ('Thirukkural', 'Thiruvalluvar', 'Tamil', 'Ancient Tamil couplets', '/ebooks/thirukkural.pdf'),
    ('Gitanjali', 'Rabindranath Tagore', 'Bengali', 'Poems of devotion', '/ebooks/gitanjali.pdf'),
    ('Panchatantra', 'Vishnu Sharma', 'Sanskrit', 'Stories with morals', '/ebooks/panchatantra.pdf')
])

conn.commit()
conn.close()
