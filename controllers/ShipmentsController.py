from controllers.InventoryItemController import updateInventoryItem, getInventoryItemById
from model.Shipments import insertShipmentItemToDB, insertShipmentDB, getShipmentsDB, getShipmentItemByIdDB, updateShipmentItemDB, deleteShipmentItemByIdDB, getShipmentItemByItemIdDB, getShipmentByIdDB

def getShipments():
  return getShipmentsDB()
  
def getShipmentById(id):
  return getShipmentByIdDB(id)

def getShipmentItemById(shipmentid, id):
  return getShipmentItemByIdDB(shipmentid, id)

def getShipmentItemByItemId(shipmentid, itemid):
  return getShipmentItemByItemIdDB(shipmentid, itemid)
  
def insertShipment(name):
  insertShipmentDB(name)
  
def insertShipmentItem(shipmentid, itemid, quantity):
  quantity = int(quantity)
  item = getInventoryItemById(itemid)
  if item is None or item['quantity'] < quantity or getShipmentById(shipmentid) is None:
    raise ValueError
  else:
    item['quantity'] = item['quantity'] - quantity
    updateInventoryItem(itemid, item)
  shipmentItem = getShipmentItemByItemIdDB(shipmentid, item['id'])
  if shipmentItem is None:
    insertShipmentItemToDB(shipmentid, item, quantity)
  else:
    updateShipmentItem(shipmentItem['id'], itemid, shipmentid, quantity + shipmentItem['quantity'])

def updateShipmentItem(id, itemid, shipmentid, quantity):
  inventoryItem = getInventoryItemById(itemid)
  shipmentItem = getShipmentItemById(shipmentid, id)
  # If inventory item exists, update the quantities in inventory list
  if inventoryItem is not None:
    if shipmentItem['quantity'] < quantity:
      addedQuantity = quantity - shipmentItem['quantity']
      if addedQuantity <= inventoryItem['quantity']:
        inventoryItem['quantity'] = inventoryItem['quantity'] - addedQuantity
        updateInventoryItem(itemid, inventoryItem)
      else:
        raise ValueError
    else:
      removedQuantity = shipmentItem['quantity'] - quantity
      inventoryItem['quantity'] = inventoryItem['quantity'] + removedQuantity
      updateInventoryItem(itemid, inventoryItem)
  updateShipmentItemDB(shipmentid, id, quantity)
      
def deleteShipmentItemById(shipmentid, itemid, id):
  inventoryItem = getInventoryItemById(itemid)
  shipmentItem = getShipmentItemById(shipmentid, id)
  # If inventory item exists, update the quantities in inventory list
  if inventoryItem is not None:
    removedQuantity = shipmentItem['quantity']
    inventoryItem['quantity'] = inventoryItem['quantity'] + removedQuantity
    updateInventoryItem(itemid, inventoryItem)
  deleteShipmentItemByIdDB(shipmentid, itemid, id)
  