from model.InventoryItem import insertInventoryItemDB, getInventoryItemsDB, updateInventoryItemDB, deleteInventoryItemByIdDB, getInventoryItemByIdDB

def getInventoryItems():
  return getInventoryItemsDB()

def getInventoryItemById(id):
  return getInventoryItemByIdDB(id)

def insertInventoryItem(item):
  item['quantity'] = int(item['quantity'])
  insertInventoryItemDB(item)

def updateInventoryItem(id, updatedItem):
  # Since ids are incremental order, find can be done more 
  # efficiently using binary search.
  updateInventoryItemDB(id, updatedItem)

def deleteInventoryItemById(id):
  deleteInventoryItemByIdDB(id)