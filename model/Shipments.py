from replit import db
from .helper import findByBinarySearch

def getShipmentsDB():
  return db["SHIPMENTS"]

def getShipmentByIdDB(id):
  shipmentIndex = findByBinarySearch(db["SHIPMENTS"], id)
  return db["SHIPMENTS"][shipmentIndex] if shipmentIndex != -1 else None

def getShipmentItemByIdDB(shipmentid, id):
  shipmentIndex = findByBinarySearch(db["SHIPMENTS"], shipmentid)
  if shipmentIndex != -1:
    itemIndex = findByBinarySearch(db["SHIPMENTS"][shipmentIndex]['itemList'], id)
    return db["SHIPMENTS"][shipmentIndex]['itemList'][itemIndex] if itemIndex != -1 else None
  else:
    return None

def getShipmentItemByItemIdDB(shipmentid, itemid):
  shipmentIndex = findByBinarySearch(db["SHIPMENTS"], shipmentid)
  if shipmentIndex != -1:
    matches = [x for x in db["SHIPMENTS"][shipmentIndex]['itemList'] if x['itemid'] == itemid]
    return matches[0] if len(matches) > 0 else None
  else:
    return None
    
def insertShipmentDB(name):
  shipment = {"name": name, "itemList": []}
  shipment['id'] = db["INCREMENTAL_ID"]['SHIPMENTS']
  db["INCREMENTAL_ID"]['SHIPMENTS'] += 1
  db["SHIPMENTS"].append(shipment)

def insertShipmentItemToDB(shipmentid, item, quantity):
  index = findByBinarySearch(db["SHIPMENTS"], shipmentid)
  if index == -1:
    raise ValueError
  newItem = {}
  newItem['id'] = db["INCREMENTAL_ID"]['SHIPMENT_ITEMS']
  db["INCREMENTAL_ID"]['SHIPMENT_ITEMS'] += 1
  newItem['itemid'] = int(item['id'])
  newItem['quantity'] = int(quantity)
  newItem['name'] = item['name']
  db["SHIPMENTS"][index]['itemList'].append(newItem)

def updateShipmentItemDB(shipmentid, id, quantity):
  shipmentIndex = findByBinarySearch(db["SHIPMENTS"], shipmentid)
  if shipmentIndex != -1:
    itemIndex = findByBinarySearch(db["SHIPMENTS"][shipmentIndex]['itemList'], id)
    if itemIndex != -1:
      db["SHIPMENTS"][shipmentIndex]['itemList'][itemIndex]['quantity'] = quantity
      return
  raise ValueError

def deleteShipmentItemByIdDB(shipmentid, itemid, id):
  shipmentIndex = findByBinarySearch(db["SHIPMENTS"], shipmentid)
  if shipmentIndex != -1:
    itemIndex = findByBinarySearch(db["SHIPMENTS"][shipmentIndex]['itemList'], id)
    if itemIndex != -1:
      db["SHIPMENTS"][shipmentIndex]['itemList'].pop(itemIndex)
      return
  raise ValueError