from flask import render_template, request, redirect, url_for, flash
from controllers.InventoryItemController import insertInventoryItem, getInventoryItems, updateInventoryItem, deleteInventoryItemById

def index():
  allItems = getInventoryItems()
  return render_template('index.html', inventory = allItems)

def addInventoryItem():
  if request.method == 'POST':
    insertInventoryItem({'name': request.form['name'],
                        'city': request.form['city'],
                        'quantity': request.form['quantity']})
    flash("Item added successfully!")
    return redirect(url_for('index'))

def editInventoryItem():
  if request.method == 'POST':
    id = request.form.get('id')
    newItem = {}
    newItem["name"] = request.form.get('name')
    newItem["city"] = request.form.get('city')
    newItem["quantity"] = request.form.get('quantity')
    updateInventoryItem(id, newItem)
    flash("Item updated successfully!")
    return redirect(url_for('index'))
    
def removeInventoryItem(id):
  deleteInventoryItemById(id)
  flash("Item deleted successfully!")
  return redirect(url_for('index'))


    
    