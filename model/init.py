from replit import db

# This function only needs to be run a single time to setup the db
def initInventoryDB():
  db["INVENTORY_ITEMS"] = []
  db["SHIPMENTS"] = []
  db["INCREMENTAL_ID"] = {
    'INVENTORY_ITEMS': 1,
    'SHIPMENTS': 1,
    'SHIPMENT_ITEMS': 1
  }
  return