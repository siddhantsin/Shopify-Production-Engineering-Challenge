from controllers.InventoryItemController import insertInventoryItem, getInventoryItems, updateInventoryItem, deleteInventoryItemById, getInventoryItemById
from model.Shipments import insertShipmentItemToDB

def insertShipmentItem(shipmentid, itemid, quantity):
  quantity = int(quantity)
  item = getInventoryItemById(itemid)
  if item['quantity'] < quantity:
    raise ValueError
  else:
    item['quantity'] = item['quantity'] - quantity
    updateInventoryItem(itemid, item)
  insertShipmentItemToDB(shipmentid, item, quantity)
  