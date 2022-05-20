from replit import db

def initInventoryDB():
  print(db["INVENTORY_ITEMS"])
  # db["INCREMENTAL_ID"] = {
  #   'INVENTORY_ITEMS': 1,
  #   'SHIPMENTS': 1,
  #   'SHIPMENT_ITEMS': 1
  # }
  return