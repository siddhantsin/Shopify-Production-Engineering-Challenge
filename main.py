import routes.ItemRoutes as ItemRoutes
import routes.ShipmentRoutes as ShipmentRoutes
from flask import Flask
from model.init import initInventoryDB

app = Flask(__name__)
app.secret_key = "SECRET"
initInventoryDB()

app.add_url_rule('/', view_func=ItemRoutes.index)
app.add_url_rule('/addInventoryItem', methods=["POST"], view_func=ItemRoutes.addInventoryItem)
app.add_url_rule('/editInventoryItem', methods=["GET", "POST"], view_func=ItemRoutes.editInventoryItem)
app.add_url_rule('/removeInventoryItem/<id>/', methods=["GET", "POST"], view_func=ItemRoutes.removeInventoryItem)

app.add_url_rule('/shipments/', view_func=ShipmentRoutes.shipmentsIndex)
app.add_url_rule('/shipments/create', methods=["POST"], view_func=ShipmentRoutes.createShipment)
app.add_url_rule('/shipments/addShipmentItem', methods=["POST"], view_func=ShipmentRoutes.addShipmentItem)
app.add_url_rule('/shipments/removeItem/<id>/<itemid>', methods=["GET", "POST"], view_func=ShipmentRoutes.removeShipmentItem)
app.add_url_rule('/shipments/editItem', methods=["GET", "POST"], view_func=ShipmentRoutes.editShipmentItem)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=81)