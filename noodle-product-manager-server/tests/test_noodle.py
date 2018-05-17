import os
import tempfile

from flask import request, jsonify
import pytest

from noodle import create_app as noodle

@pytest.fixture
def client():
    """ Configure the test client """
    client = noodle()
    yield client.test_client()

def test_create_product(client):
    """ Create a product """

    json_input = {"data":{"attributes":{"name":"Sample product"},
                          "type":"products"}}
    response = client.post('/api/products', json=json_input)
    json_data = response.get_json()['data']['attributes']['name']
    assert json_data == 'Sample product', 'Product name is returned'

def test_show_product_list(client):
    """ Show all products """

    response = client.get('/api/products')
    json_data = response.get_json()
    assert len(json_data) > 0, 'Return all products in the db'

def test_create_detail(client):
    """ Create an detail """

    json_input = {"data":{"attributes":{"name":"Sample detail"},
                          "type":"details"}}
    response = client.post('/api/details', json=json_input)
    json_data = response.get_json()['data']['attributes']['name']
    assert json_data == 'Sample detail', 'detail name is returned'

def test_show_detail_list(client):
    """ Show all details """

    response = client.get('/api/details')
    json_data = response.get_json()
    assert len(json_data) > 0, 'Return all details in the db'
