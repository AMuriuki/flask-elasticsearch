import traceback
from app.models import Product, ProductCategory, ProductCollection, ProductType
from app import db
import os
import json
from flask import current_app


def get_data():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "data.json")
    data = json.load(open(json_url))
    return data


def dummy_data():
    try:
        products = get_data()
        for product in products:
            product_exists = Product.query.filter_by(
                title=product['title']).first()

            if not product_exists:
                category_name = (product['categories'][0]).strip()

                category = ProductCategory.query.filter_by(
                    name=category_name).first()

                if category:
                    category_id = category.id
                else:
                    new_category = ProductCategory(
                        name=category_name)
                    db.session.add(new_category)
                    db.session.commit()
                    category_id = new_category.id

                collection_name = (product['categories'][1]).strip()

                collection = ProductCollection.query.filter_by(
                    name=collection_name).first()

                if collection:
                    collection_id = collection.id
                else:
                    new_collection = ProductCollection(
                        name=collection_name, category=category_id)
                    db.session.add(new_collection)
                    db.session.commit()
                    collection_id = new_collection.id

                type_name = (product['categories'][2]).strip()

                product_type = ProductType.query.filter_by(
                    name=type_name).first()

                if product_type:
                    type_id = product_type.id
                else:
                    new_type = ProductType(
                        name=type_name, collection_id=collection_id, category_id=category_id)
                    db.session.add(new_type)
                    db.session.commit()
                    type_id = new_type.id
                
                record = Product(
                    title=product['title'], product_category=category_id, product_type=type_id, product_collection=collection_id, in_stock=get_value('in_stock', product), price=clean_price(product['price']), description=get_value('product_details', product), rating=get_value('rating', product), store=get_value('store', product), brand=product['brand'], original_price=clean_price(get_value('original_price', product)), discount=clean_discount(get_value('discount', product)))

                db.session.add(record)
                db.session.commit()                
            else:
                # update product
                product_exists.in_stock = get_value('in_stock', product)
                product_exists.price = clean_price(product['price'])
                db.session.commit()
    except Exception as e:
        current_app.logger.error(e)
        current_app.logger.debug(traceback.format_exc())


def clean_price(raw):
    if raw:
        # remove Ksh
        clean = raw.replace("KSh", "").replace(",", "").strip()
        if " - " in clean:
            clean = clean.split(" - ")[0]
        # convert str to float
        cleaned = float(clean)
        return cleaned
    else:
        return None


def clean_discount(raw):
    if raw:
        # remove %
        clean = raw.replace("%", "").strip()
        # convert str to float
        cleaned = float(clean)
        return cleaned
    else:
        return None


# if key exists in dict return value else return None
def get_value(key, dict):
    if key in dict:
        return dict[key]
    else:
        return None
