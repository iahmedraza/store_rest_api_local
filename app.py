from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserRegister, User
from resources.item import Item, ItemList
from db import db
from resources.store import Store, StoreList
import os
app = Flask(__name__)
uri =  "sqlite:///data.db" 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_DATABASE_URI"] = uri 
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = "Ahmed"
api = Api(app)

jwt = JWT(app, authenticate, identity)


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(User, '/user/<int:user_id>')

if __name__ == "__main__":
    db.init_app(app)
    
    if app.config['DEBUG']:
        @app.before_first_request
        def create_tables():
            db.create_all()

    app.run(port=5000, debug= True)
