#!/usr/bin/env python
from flask import Flask
from flask import jsonify 
from flask_jwt_extended import JWTManager
from flask_jwt_extended import jwt_required
from flask_cors import CORS

from core.sqlalchemy import db
from config.db_config import URI
from core.marshmallow import ma
from resources.login import Login
from resources.user import User
from resources.user import UsersLevel
from resources.user import UsersStatus
from resources.client import Client
from resources.client import ClientType
from resources.client import ClientStatus
from resources.product import Product
from resources.product import ProductCategory
from resources.product import ProductStatus
from resources.product import ProductCommercialBrand
from resources.provider import Provider
from resources.provider import ProviderStatus
from resources.provider import ProviderReputation
from resources.inventory_flow import InventoryFlow
from resources.inventory_flow import InventoryFlowType
from resources.sale import Sale
from resources.sale import SaleStatus
from resources.sold_products import SoldProducts
from resources.logout import LogOut
from errors.token_handler import TokenErrorHandler

app = Flask(__name__)
CORS(app)
app.config['JSON_SORT_KEYS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 60 * 60
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access']

jwt = JWTManager(app)
db.init_app(app)
ma.init_app(app)
blacklist = set()

login = Login()
log_out = LogOut(blacklist)
jwt.token_in_blacklist_loader(log_out.check_if_token_in_blacklist)
jwt.revoked_token_loader(TokenErrorHandler.revoken_token)
jwt.unauthorized_loader(TokenErrorHandler.unauthorized_token)
jwt.expired_token_loader(TokenErrorHandler.expired_token)


user = User()
user_level = UsersLevel()
user_status = UsersStatus()
client = Client()
client_type = ClientType()
client_status = ClientStatus()
product = Product()
product_category = ProductCategory()
product_status = ProductStatus()
product_commercial_brand = ProductCommercialBrand()
provider = Provider()
provider_status = ProviderStatus()
provider_reputation = ProviderReputation()
inventory_flow = InventoryFlow()
inventory_flow_type = InventoryFlowType()
sale = Sale()
sale_status = SaleStatus()
sold_products = SoldProducts()

app.add_url_rule('/login/', view_func=login.login)
app.add_url_rule('/users/', view_func=user.user_r)
app.add_url_rule('/users/level/', view_func=user_level.user_level_r)
app.add_url_rule('/users/status/', view_func=user_status.user_status_r)
app.add_url_rule('/clients/', view_func=client.client_r)
app.add_url_rule('/clients/type/', view_func=client_type.client_type_r)
app.add_url_rule('/clients/status/', view_func=client_status.client_status_r)
app.add_url_rule('/products/', view_func=product.product_r)
app.add_url_rule('/products/categories/', view_func=product_category.product_category_r)
app.add_url_rule('/products/status/', view_func=product_status.product_status_r)
app.add_url_rule('/products/commercial-brands/', view_func=product_commercial_brand.product_commercial_brand_r)
app.add_url_rule('/providers/', view_func=provider.provider_r)
app.add_url_rule('/providers/reputation/', view_func=provider_reputation.provider_reputation_r)
app.add_url_rule('/providers/status/', view_func=provider_status.provider_status_r)
app.add_url_rule('/inventory-flow/', view_func=inventory_flow.inventory_flow_r)
app.add_url_rule('/inventory-flow/type/', view_func=inventory_flow_type.inventory_flow_type_r)
app.add_url_rule('/sale/', view_func=sale.sale_r)
app.add_url_rule('/sale/status/', view_func=sale_status.sale_status_r)
app.add_url_rule('/sale/<id>/sold-products/', view_func=sold_products.sold_products_r)
app.add_url_rule('/log-out/', view_func=log_out.logout)

@app.route('/check-access-token/', methods=['GET'])
@jwt_required
def check_access_token():
	return jsonify('CHECKED'), 200

@app.errorhandler(404)
def not_found_error(error):
    return jsonify(Error='Parece que tienes errores en los parametros de busqueda'), 400

if __name__ == "__main__":
	app.run(use_debugger=True, host= "0.0.0.0", port=17499, use_reloader=True)