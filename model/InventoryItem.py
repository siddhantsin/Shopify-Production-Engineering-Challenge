from replit import db
from .helper import findByBinarySearch

def getInventoryItemsDB():
  return db["INVENTORY_ITEMS"]

def getInventoryItemByIdDB(id):
  index = findByBinarySearch(db["INVENTORY_ITEMS"], id)
  return db["INVENTORY_ITEMS"][index] if index != -1 else None

def insertInventoryItemDB(item):
  item['id'] = db["INCREMENTAL_ID"]['INVENTORY_ITEMS']
  db["INCREMENTAL_ID"]['INVENTORY_ITEMS'] += 1
  db["INVENTORY_ITEMS"].append(item)

def updateInventoryItemDB(id, updatedItem):
  # Since ids are incremental order, find can be done more 
  # efficiently using binary search.
  index = findByBinarySearch(db["INVENTORY_ITEMS"], id)
  if index == -1:
    raise ValueError
  updatedItem['id'] = int(id)
  db["INVENTORY_ITEMS"][index] = updatedItem

def deleteInventoryItemByIdDB(id):
  index = findByBinarySearch(db["INVENTORY_ITEMS"], id)
  if index == -1:
    raise ValueError
  db["INVENTORY_ITEMS"].pop(index)
