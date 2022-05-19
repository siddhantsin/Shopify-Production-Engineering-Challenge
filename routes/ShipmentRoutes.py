from flask import render_template, request, redirect, url_for, flash
from controllers.InventoryItemController import insertInventoryItem, getInventoryItems, updateInventoryItem, deleteInventoryItemById, getInventoryItemById
from model.Shipments import insertShipment, getShipments
from controllers.ShipmentsController import insertShipmentItem

def shipmentsIndex():
  allItems = getShipments()
  return render_template('shipments.html', shipments = allItems)

def createShipment():
  if request.method == 'POST':
    insertShipment(request.form['name'])
    flash("Shipment added successfully!")
    return redirect(url_for('shipmentsIndex'))

def addShipmentItem():
  if request.method == 'POST':
    itemid = request.form.get('itemid')
    shipmentid = request.form.get('shipmentid')
    quantity = request.form.get('quantity')
    insertShipmentItem(shipmentid, itemid, quantity)
    flash("Added item to shipment successfully!")
    return redirect(url_for('shipmentsIndex'))
    
def editShipmentItem():
  if request.method == 'POST':
    id = request.form.get('id')
    newItem = {}
    newItem["name"] = request.form.get('name')
    newItem["city"] = request.form.get('city')
    newItem["quantity"] = request.form.get('quantity')
    updateInventoryItem(id, newItem)
    flash("Item updated successfully!")
    return redirect(url_for('shipmentsIndex'))
    
def removeShipmentItem(id):
  deleteInventoryItemById(id)
  flash("Item deleted successfully!")
  return redirect(url_for('shipmentsIndex'))