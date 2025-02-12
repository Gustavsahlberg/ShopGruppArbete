from models import Category, Product


def getTrendingCategories():
    return Category.query.order_by(Category.CategoryID.desc()).paginate(page=1,per_page=4,error_out=False).items

def getCategory(id):
    return Category.query.filter(Category.CategoryID ==id).first()

def getProduct(id):
    return Product.query.filter(Product.ProductID ==id).first()

def getTrendingProducts(sort_by="latest"):

    if sort_by == "price":
        return Product.query.order_by(Product.UnitPrice.asc()).paginate(page=1,per_page=8,error_out=False).items
    elif sort_by == "name":
        return Product.query.order_by(Product.ProductName.asc()).paginate(page=1,per_page=8,error_out=False).items
    elif sort_by == "asc":
        return Product.query.order_by(Product.ProductID.asc()).paginate(page=1,per_page=8,error_out=False).items
    else:
        return Product.query.order_by(Product.ProductID.desc()).paginate(page=1,per_page=8,error_out=False).items
