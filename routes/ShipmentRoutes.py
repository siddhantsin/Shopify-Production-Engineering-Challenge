from flask import render_template, request, redirect, url_for, flash
from controllers.ShipmentsController import insertShipmentItem, insertShipment, getShipments, updateShipmentItem, deleteShipmentItemById

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
    insertShipmentItem(int(shipmentid), int(itemid), int(quantity))
    flash("Added item to shipment successfully!")
    return redirect(url_for('shipmentsIndex'))
    
def editShipmentItem():
  if request.method == 'POST':
    id = request.form.get('id')
    itemid = request.form.get('itemid')
    shipmentid = request.form.get('shipmentid')
    quantity = request.form.get('quantity')
    updateShipmentItem(int(id), int(itemid), int(shipmentid), int(quantity))
    flash("Item updated successfully!")
    return redirect(url_for('shipmentsIndex'))
    
def removeShipmentItem(shipmentid, itemid, id):
  deleteShipmentItemById(int(shipmentid), int(itemid), int(id))
  flash("Item deleted successfully!")
  return redirect(url_for('shipmentsIndex'))