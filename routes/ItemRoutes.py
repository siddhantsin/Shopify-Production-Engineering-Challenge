from flask import render_template, request, redirect, url_for, flash
from controllers.InventoryItemController import insertInventoryItem, getInventoryItems, updateInventoryItem, deleteInventoryItemById
from services.weather import getWeatherInfo

async def index():
  if request.method == 'GET':
    weatherData = await getWeatherInfo()
    allItems = getInventoryItems()
    return render_template('index.html', inventory = allItems, weather = weatherData)

def addInventoryItem():
  if request.method == 'POST':
    insertInventoryItem({'name': request.form['name'],
                        'city': request.form['city'],
                        'quantity': int(request.form['quantity'])})
    flash("Item added successfully!")
    return redirect(url_for('index'))

def editInventoryItem():
  try:
    if request.method == 'POST':
      id = request.form.get('id')
      newItem = {}
      newItem["name"] = request.form.get('name')
      newItem["city"] = request.form.get('city')
      newItem["quantity"] = int(request.form.get('quantity'))
      updateInventoryItem(int(id), newItem)
      flash("Item updated successfully!")
      return redirect(url_for('index'))
  except ValueError:
    flash("Please input correct values")
    return redirect(url_for('index'), code=400)
    
def removeInventoryItem(id):
  try:
    deleteInventoryItemById(int(id))
    flash("Item deleted successfully!")
    return redirect(url_for('index'))
  except ValueError:
    flash("Please input correct values")
    return redirect(url_for('index'), code=400)
    


    
    