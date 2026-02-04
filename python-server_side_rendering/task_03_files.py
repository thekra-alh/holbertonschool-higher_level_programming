#!/usr/bin/python3
"""
Flask application for displaying data from JSON or CSV files.
"""

import json
import csv
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


@app.route('/products')
def products():
    """Display products from JSON or CSV based on source parameter."""
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    
    # Check for valid source
    if source not in ['json', 'csv']:
        return render_template('product_display.html', 
                             error="Wrong source")
    
    # Read data based on source
    if source == 'json':
        products_data = read_json_file('products.json')
    else:  # csv
        products_data = read_csv_file('products.csv')
    
    # Handle file reading errors
    if products_data is None:
        return render_template('product_display.html', 
                             error="Error reading file")
    
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
