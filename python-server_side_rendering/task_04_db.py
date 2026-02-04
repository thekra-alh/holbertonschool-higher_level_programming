 #!/usr/bin/python3
"""
Flask application for displaying data from JSON, CSV, or SQLite database.
"""

import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json_file(filename):
    """Read and return data from a JSON file."""
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        return None


def read_csv_file(filename):
    """Read and return data from a CSV file."""
    try:
        products = []
        with open(filename, 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                # Convert id to int and price to float
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
        return products
    except FileNotFoundError:
        return None
    except (ValueError, KeyError):
        return None


def read_sqlite_db(db_name):
    """Read and return data from a SQLite database."""
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products')
        rows = cursor.fetchall()
        conn.close()
        
        # Convert to list of dictionaries
        products = []
        for row in rows:
            products.append({
                'id': row[0],
                'name': row[1],
                'category': row[2],
                'price': row[3]
            })
        return products
    except sqlite3.Error:
        return None


@app.route('/products')
def products():
    """Display products from JSON, CSV, or SQLite based on source parameter."""
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    
    # Check for valid source
    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', 
                             error="Wrong source")
    
    # Read data based on source
    if source == 'json':
        products_data = read_json_file('products.json')
    elif source == 'csv':
        products_data = read_csv_file('products.csv')
    else:  # sql
        products_data = read_sqlite_db('products.db')
    
    # Handle file/database reading errors
    if products_data is None:
        return render_template('product_display.html', 
                             error="Error reading data source")
    
    # Filter by ID if provided
    if product_id is not None:
        products_data = [p for p in products_data if p['id'] == product_id]
        if not products_data:
            return render_template('product_display.html', 
                                 error="Product not found")
    
    return render_template('product_display.html', 
                         products=products_data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
