from model.InventoryItem import insertInventoryItemDB, getInventoryItemsDB, updateInventoryItemDB, deleteInventoryItemByIdDB, getInventoryItemByIdDB

def getInventoryItems():
  allItems = getInventoryItemsDB()
  return allItems

def getInventoryItemById(id):
  return getInventoryItemByIdDB(id)

def insertInventoryItem(item):
  insertInventoryItemDB(item)

def updateInventoryItem(id, updatedItem):
  updateInventoryItemDB(id, updatedItem)

def deleteInventoryItemById(id):
  deleteInventoryItemByIdDB(id)