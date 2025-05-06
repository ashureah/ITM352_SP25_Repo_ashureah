from flask import Flask, render_template, request, redirect, url_for
import json
import os
from datetime import datetime, timedelta

app = Flask(__name__)
INVENTORY_FILE = 'inventory.json'

def load_inventory():
    if os.path.exists(INVENTORY_FILE):
        with open(INVENTORY_FILE, 'r') as file:
            return json.load(file)
    return []

def save_inventory(inventory):
    with open(INVENTORY_FILE, 'w') as file:
        json.dump(inventory, file, indent=4)

@app.route('/')
def home():
    return render_template('index.html')

@app.sroute('/add', methods=['GET', 'POST'])
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
    sort_by = request.args.get('sort_by', 'category')
    inventory.sort(key=lambda x: x.get(sort_by, ''))
    return render_template('view.html', inventory=inventory)

@app.route('/alerts')
def alerts():
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

    return render_template('view.html', inventory=expired + expiring)

@app.route('/search', methods=['GET'])
def search():
    term = request.args.get('q', '').lower()
    inventory = load_inventory()
    results = [item for item in inventory if term in item['name'].lower() or term in item['category'].lower()]
    return render_template('search.html', inventory=results, term=term)

@app.route('/delete/<name>')
def delete(name):
    inventory = load_inventory()
    inventory = [item for item in inventory if item['name'].lower() != name.lower()]
    save_inventory(inventory)
    return redirect(url_for('view'))

if __name__ == '__main__':
    app.run(debug=True)
