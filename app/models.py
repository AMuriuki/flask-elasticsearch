from flask import url_for
from app import db
from datetime import datetime


class PaginatedAPIMixin(object):
    @staticmethod
    def to_collection_dict(query, page, per_page, endpoint, **kwargs):
        resources = query.paginate(page=page, per_page=per_page,
                                   error_out=False)
        data = {
            'items': [item.to_dict() for item in resources.items],
            '_meta': {
                'page': page,
                'per_page': per_page,
                'total_pages': resources.pages,
                'total_items': resources.total
            },
            '_links': {
                'self': url_for(endpoint, page=page, per_page=per_page,
                                **kwargs),
                'next': url_for(endpoint, page=page + 1, per_page=per_page,
                                **kwargs) if resources.has_next else None,
                'prev': url_for(endpoint, page=page - 1, per_page=per_page,
                                **kwargs) if resources.has_prev else None
            }
        }
        return data


class Product(db.Model, PaginatedAPIMixin):
    id = db.Column(db.Integer, primary_key=True)
    product_category = db.Column(
        db.Integer, db.ForeignKey('product_category.id'))
    product_type = db.Column(db.Integer, db.ForeignKey(
        'product_type.id'), nullable=True)
    product_collection = db.Column(db.Integer, db.ForeignKey(
        'product_collection.id'), nullable=True)
    title = db.Column(db.Text())
    description = db.Column(db.Text())
    created_on = db.Column(db.DateTime, default=datetime.utcnow)
    updated_on = db.Column(db.DateTime, default=datetime.utcnow)
    published_on = db.Column(db.DateTime)
    rating = db.Column(db.String(120))
    is_draft = db.Column(db.Boolean, default=True)
    is_published = db.Column(db.Boolean, default=False)
    in_stock = db.Column(db.String(120))
    slug = db.Column(db.Text(), unique=True)
    price = db.Column(db.Float())
    original_price = db.Column(db.Float())
    discount = db.Column(db.Float())
    brand = db.Column(db.String(120))
    store = db.Column(db.String(120))

    def __repr__(self):
        return self.title

    def from_dict(self, data, new_product=False):
        for field in ['title', 'description']:
            if field in data:
                setattr(self, field, data[field])

    def to_dict(self):
        data = {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'sku': self.sku,
            'slug': self.slug
        }
        return data


class ProductCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)
    products = db.relationship('Product', backref='category', lazy='dynamic')
    collections = db.relationship(
        'ProductCollection', backref='parent', lazy='dynamic')
    product_types = db.relationship(
        'ProductType', backref='parent', lazy='dynamic')

    def count_collections(self):
        collections = self.collections.count()
        return collections

    def count_types(self):
        types = self.product_types.count()
        return types

    def count_products(self):
        products = self.products.count()
        return products


class ProductType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)
    products = db.relationship('Product', backref='type', lazy='dynamic')
    parent_id = db.Column(db.Integer, db.ForeignKey('product_category.id'))


class ProductCollection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)
    products = db.relationship('Product', backref='collection', lazy='dynamic')
    category = db.Column(db.Integer, db.ForeignKey('product_category.id'))
    product_types = db.relationship(
        'ProductType', backref='parent_collection', lazy='dynamic')