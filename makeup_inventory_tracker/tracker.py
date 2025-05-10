from flask import Flask, render_template, request, redirect, url_for
import json
import os
from datetime import datetime, timedelta

app = Flask(__name__)
INVENTORY_FILE = 'inventory.json'

def load_inventory():
    if os.path.exists(INVENTORY_FILE):
        with open(INVENTORY_FILE, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []


def save_inventory(inventory):
    with open(INVENTORY_FILE, 'w') as file:
        json.dump(inventory, file, indent=4)

# Homepage: search, quick links, and expiration preview
@app.route('/')
def home():
    today = datetime.today().date()
    inventory = load_inventory()
    expiring = []
    expired = []

    for item in inventory:
        exp_date = datetime.strptime(item['expiration_date'], "%Y-%m-%d").date()
        days_left = (exp_date - today).days
        if days_left < 0:
            expired.append(item)
        elif days_left <= 30:
            expiring.append(item)

    return render_template('index.html', expired=expired, expiring=expiring)

# Add a new product to the inventory
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        product = {
            "name": request.form['name'],
            "brand": request.form['brand'],
            "category": request.form['category'],
            "purchase_date": request.form['purchase_date'],
            "expiration_date": request.form['expiration_date']
        }
        inventory = load_inventory()
        inventory.append(product)
        save_inventory(inventory)
        return redirect(url_for('view'))
    return render_template('add.html')

@app.route('/view')
def view():
    inventory = load_inventory()
    today = datetime.today().date()

    for item in inventory:
        exp_date = datetime.strptime(item['expiration_date'], "%Y-%m-%d").date()
        days_left = (exp_date - today).days
        if days_left < 0:
            item['status'] = 'expired'
        elif days_left <= 30:
            item['status'] = 'expiring'
        else:
            item['status'] = 'safe'

    sort_by = request.args.get('sort_by', 'category')
    inventory.sort(key=lambda x: x.get(sort_by, ''))

    return render_template('view.html', inventory=inventory)

# Show only expired products
@app.route('/alerts')
def alerts():
    today = datetime.today().date()
    inventory = load_inventory()
    expired = []

    for item in inventory:
        exp_date = datetime.strptime(item['expiration_date'], "%Y-%m-%d").date()
        days_left = (exp_date - today).days
        if days_left < 0:
            item['status'] = 'expired'
            expired.append(item)

    return render_template('alerts.html', inventory=expired)

# Search inventory by name, brand, or category
@app.route('/search', methods=['GET'])
def search():
    term = request.args.get('q', '').lower()
    inventory = load_inventory()

    # Precompute status just like in /view
    today = datetime.today().date()
    for item in inventory:
        exp_date = datetime.strptime(item['expiration_date'], "%Y-%m-%d").date()
        days_left = (exp_date - today).days
        if days_left < 0:
            item['status'] = 'expired'
        elif days_left <= 30:
            item['status'] = 'expiring'
        else:
            item['status'] = 'safe'

    results = [
        item for item in inventory
        if term in item['name'].lower() or term in item['brand'].lower() or term in item['category'].lower()
    ]

    return render_template('search.html', inventory=results, term=term)

@app.route('/delete/<name>')
def delete(name):
    inventory = load_inventory()
    inventory = [item for item in inventory if item['name'].lower() != name.lower()]
    save_inventory(inventory)
    return redirect(url_for('view'))

if __name__ == '__main__':
    app.run(debug=True)
