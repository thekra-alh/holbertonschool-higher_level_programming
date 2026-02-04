#!/usr/bin/python3
"""
Script to create and populate the SQLite database for products.
"""

import sqlite3


def create_database():
    """Create the products database and populate it with initial data."""
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    
    # Drop table if exists to start fresh
    cursor.execute('DROP TABLE IF EXISTS Products')
    
    # Create Products table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    
    # Insert sample data
    cursor.execute('''
        INSERT INTO Products (id, name, category, price)
        VALUES
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99)
    ''')
    
    conn.commit()
    conn.close()
    print("Database created successfully!")


if __name__ == '__main__':
    create_database()
