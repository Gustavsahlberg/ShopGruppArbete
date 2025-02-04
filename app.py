from flask import Flask, render_template
from models import db, seedData
from flask_migrate import Migrate, upgrade
from areas.site.sitePages import siteBluePrint
from areas.products.productPages import productBluePrint

app = Flask(__name__)
app.config.from_object('config.ConfigDebug')

db.app = app
db.init_app(app)
migrate = Migrate(app,db)


app.register_blueprint(siteBluePrint)
app.register_blueprint(productBluePrint)

if __name__  == "__main__":
    with app.app_context():
        upgrade()
        seedData(app)
        app.run()


