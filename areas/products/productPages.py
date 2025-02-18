from flask import Blueprint, render_template,request
from forms import NewsLetterForm
from models import Newsletter, db
from flask_mail import Message
from .services import getCategory, getTrendingCategories, getProduct, getTrendingProducts



productBluePrint = Blueprint('product', __name__)




@productBluePrint.route('/',  methods=["GET", "POST"])
def index() -> str:
    form = NewsLetterForm()
    if request.method == "POST":
        new_reg = Newsletter()
        new_reg.email = form.email.data
        finns = Newsletter.query.filter_by(email=new_reg.email).first()
        if finns is None:
            db.session.add(new_reg)
            db.session.commit()
            msg = Message(
            'Bekräftelse Newsletter',
            recipients=[new_reg.email],
            body="Du har nu premenurerat på newsletter till Stefans Supershop"
            )
            mail.send(msg)
            return render_template("site/contactthanks.html",form=form)
        else:
            return 

        
    trendingCategories = []
    trendingCategories = getTrendingCategories()

    sort_by = request.args.get('sort', "latest")
    trendingProducts = getTrendingProducts(sort_by)
    return render_template('products/index.html',trendingCategories=trendingCategories,
        products=trendingProducts,
        sort_by=sort_by,
        form=form
    )


@productBluePrint.route('/category/<id>')
def category(id) -> str:
    category = getCategory(id)
    return render_template('products/category.html',category=category)

@productBluePrint.route('/product/<id>')
def product(id) -> str:
    product = getProduct(id)
    return render_template('products/product.html',product=product)




