from flask import Flask
from models import db, seedData
from flask_migrate import Migrate, upgrade
from areas.site.sitePages import siteBluePrint
from areas.products.productPages import productBluePrint
from flask_mail import Mail

import os

app = Flask(__name__)
app.config.from_object('config.ConfigDebug')

mail = Mail()
db.app = app
db.init_app(app)
migrate = Migrate(app,db)
mail.init_app(app)

app.secret_key = os.getenv("SECRET_KEY")

app.register_blueprint(siteBluePrint)
app.register_blueprint(productBluePrint)

if __name__  == "__main__":
    with app.app_context():
        upgrade()
        seedData(app)
        app.run()


