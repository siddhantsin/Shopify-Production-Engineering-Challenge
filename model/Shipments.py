from replit import db
from .helper import findByBinarySearch

def getShipments():
  return db["SHIPMENTS"]
  
def insertShipment(name):
  shipment = {"name": name, "itemList": []}
  allItems = db["SHIPMENTS"]
  if len(allItems) > 0:
    lastItemId = allItems[-1]["id"]
    shipment['id'] = lastItemId + 1
  else:
    shipment['id'] = 1
  db["SHIPMENTS"].append(shipment)

def insertShipmentItemToDB(shipmentid, item, quantity):
  index = findByBinarySearch(db["SHIPMENTS"], shipmentid)
  allItems = db["SHIPMENTS"][index]['itemList']
  newItem = {}
  if len(allItems) > 0:
    lastItemId = allItems[-1]["id"]
    newItem['id'] = lastItemId + 1
  else:
    newItem['id'] = 1
  newItem['itemid'] = item['id']
  newItem['quantity'] = quantity
  newItem['name'] = item['name']
  db["SHIPMENTS"][index]['itemList'].append(newItem)