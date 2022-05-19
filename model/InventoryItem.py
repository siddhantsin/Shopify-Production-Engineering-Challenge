from replit import db
from .helper import findByBinarySearch

def getInventoryItemsDB():
  return db["INVENTORY_ITEMS"]

def getInventoryItemByIdDB(id):
  index = findByBinarySearch(db["INVENTORY_ITEMS"], id)
  return db["INVENTORY_ITEMS"][index] if index != -1 else None

def insertInventoryItemDB(item):
  allItems = db["INVENTORY_ITEMS"]
  if len(allItems) > 0:
    lastItemId = allItems[-1]["id"]
    item['id'] = int(lastItemId) + 1
  else:
    item['id'] = 1
  db["INVENTORY_ITEMS"].append(item)

def updateInventoryItemDB(id, updatedItem):
  # Since ids are incremental order, find can be done more 
  # efficiently using binary search.
  index = findByBinarySearch(db["INVENTORY_ITEMS"], id)
  updatedItem['id'] = int(id)
  db["INVENTORY_ITEMS"][index] = updatedItem

def deleteInventoryItemByIdDB(id):
  index = findByBinarySearch(db["INVENTORY_ITEMS"], id)
  db["INVENTORY_ITEMS"].pop(index)
