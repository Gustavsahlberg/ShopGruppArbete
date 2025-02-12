from flask import Blueprint, render_template,request
from .services import getCategory, getTrendingCategories, getProduct, getTrendingProducts



productBluePrint = Blueprint('product', __name__)




@productBluePrint.route('/')
def index() -> str:
    trendingCategories = []
    trendingCategories = getTrendingCategories()

    sort_by = request.args.get('sort', "latest")
    trendingProducts = getTrendingProducts(sort_by)
    return render_template('products/index.html',trendingCategories=trendingCategories,
        products=trendingProducts,
        sort_by=sort_by
    )


@productBluePrint.route('/category/<id>')
def category(id) -> str:
    category = getCategory(id)
    return render_template('products/category.html',category=category)

@productBluePrint.route('/product/<id>')
def product(id) -> str:
    product = getProduct(id)
    return render_template('products/product.html',product=product)




