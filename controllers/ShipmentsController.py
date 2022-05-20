from controllers.InventoryItemController import updateInventoryItem, getInventoryItemById
from model.Shipments import insertShipmentItemToDB, insertShipmentDB, getShipmentsDB, getShipmentItemByIdDB, updateShipmentItemDB, deleteShipmentItemByIdDB

def getShipments():
  return getShipmentsDB()

def getShipmentItemById(shipmentid, id):
  return getShipmentItemByIdDB(shipmentid, id)
  
def insertShipment(name):
  insertShipmentDB(name)
  
def insertShipmentItem(shipmentid, itemid, quantity):
  quantity = int(quantity)
  item = getInventoryItemById(itemid)
  if item['quantity'] < quantity or item is None:
    raise ValueError
  else:
    item['quantity'] = item['quantity'] - quantity
    updateInventoryItem(itemid, item)
  insertShipmentItemToDB(shipmentid, item, quantity)

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
  