# coding=utf-8
""" Main entry point """

from flask import Flask, jsonify, request
from flask_cors import CORS

from .entities.entity import Session, engine, Base
from .entities.product import Product, ProductSchema
from .entities.detail import Detail, DetailSchema


# generate database schema
Base.metadata.create_all(engine)


def create_app(test_config=None):
    """ Create the flask app """
    app = Flask(__name__)
    if not test_config:
        app.config.from_pyfile('config.py', silent=True)
    if test_config:
        app.config.from_pyfile('test_config.py', silent=True)
    app.base_url = '/api'
    CORS(app)

    # Product Endpoints

    @app.route('/api/products')
    def get_products():
        """ Get all products from the database """
        session = Session()
        product_objects = session.query(Product).all()

        schema = ProductSchema(many=True, include_data=('details',))
        products = schema.dump(product_objects)

        session.close()
        return jsonify(products.data)

    @app.route('/api/products/<int:product_id>')
    def get_product(product_id):
        """ Get a specific product from the database """
        session = Session()
        product_object = session.query(Product).get(product_id)

        schema = ProductSchema(include_data=('details',))
        product = schema.dump(product_object)

        session.close()
        return jsonify(product.data)

    @app.route('/api/products', methods=['POST'])
    def add_product():
        """ Add a product to the database """
        session = Session()
        posted_product = ProductSchema(include_data=('details',)).load(request.get_json())

        product = Product(posted_product.data['name'], created_by="Posted from client")
        _set_details(session, product, posted_product.data['details'])

        session.add(product)
        session.commit()

        new_product = ProductSchema().dump(product).data
        session.close()
        return jsonify(new_product), 201

    @app.route('/api/products/<int:product_id>', methods=["PUT", "PATCH"])
    def update_product(product_id):
        """ Update a specific product in the database """
        session = Session()
        schema = ProductSchema(include_data=('details',))

        product = session.query(Product).get(product_id)
        posted_product = schema.load(request.get_json())
        product.name = posted_product.data.get('name', product.name)
        _set_details(session, product, posted_product.data['details'])

        session.commit()
        result = schema.dump(product).data
        session.close()
        return jsonify(result)

    @app.route('/api/products/<int:product_id>', methods=["DELETE"])
    def delete_product(product_id):
        """ Delete a specific product from the database """
        session = Session()
        product_object = session.query(Product).get(product_id)
        session.delete(product_object)
        session.commit()

        session.close()
        return '', 204

    # Details Endpoints

    @app.route('/api/details')
    def get_details():
        """ Get all details from the database """
        session = Session()
        detail_objects = session.query(Detail).all()

        schema = DetailSchema(many=True)
        details = schema.dump(detail_objects)

        session.close()
        return jsonify(details.data)

    @app.route('/api/details/<int:detail_id>')
    def get_detail(detail_id):
        """ Get a specific detail from the database """
        session = Session()
        detail_object = session.query(Detail).get(detail_id)

        schema = DetailSchema()
        detail = schema.dump(detail_object)

        session.close()
        return jsonify(detail.data)

    @app.route('/api/details', methods=['POST'])
    def add_detail():
        """ Add a detail to the database """
        posted_detail = DetailSchema().load(request.get_json())

        detail = Detail(**posted_detail.data,
                              created_by="Posted from client")

        session = Session()
        session.add(detail)
        session.commit()

        new_detail = DetailSchema().dump(detail).data
        session.close()
        return jsonify(new_detail), 201

    @app.route('/api/details/<int:detail_id>', methods=["PUT", "PATCH"])
    def update_detail(detail_id):
        """ Update a specific detail in the database """
        session = Session()
        schema = DetailSchema()

        detail_query = session.query(Detail).filter(Detail.id ==
                                                          detail_id)
        detail_query.update(request.get_json())

        detail = schema.dump(detail_query.one())

        session.close()
        return jsonify(detail.data)

    @app.route('/api/details/<int:detail_id>', methods=["DELETE"])
    def delete_detail(detail_id):
        """ Delete a specific detail from the database """
        session = Session()
        detail_object = session.query(Detail).get(detail_id)
        session.delete(detail_object)

        session.close()
        return '', 204

    def _set_details(session, product, new_detail_ids):
        new_details = session.query(Detail).filter(
                Detail.id.in_(new_detail_ids)).all()
        product.details.clear()
        product.details = new_details


    return app

