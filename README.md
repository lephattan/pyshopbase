# pyshopbase
A python wrapper for Shopbase Api. View [Shopbase Api Docs](https://api-doc.shopbase.com/) for more reference.

## Installation

*Requirement: Python 3.5

```
git clone https://github.com/lephattan/pyshopbase.git
python setup.py install
```

## Getting started
* Generate API Credentitals (API Key and Password) following this intructions: https://developers.shopbase.com/build-an-app-tutorial/making-your-first-request
* Check out the Shopbase API endpoints and data that can be manipulated in: https://api-doc.shopbase.com/

## Setup ```pyshopbase::API()```
```python
from pyshopbase import API

sbapi = API(
    shop='yourshop.onshopbase.com',
    key='your-api-key',
    password='your-api-password'
)
```
### Options:
|Option|Type|Required|Description|
|----|:----:|:----:|:----|
|shop|str|yes|Your store url without the "https://"|
|key|str|yes|Your Api Key|
|password|str|yes|Your Api Password|
|scope|str|no| Your API scope. default: ```admin```|
|timeout|int|no|API request timeout (secs). default:```60```|

## Response ```pyshopbase::Response()```

All request will return Response Object. Example of returned data:

```python
r = sbapi.get('orders')
r.status_code
>>> 200
r.json
>>> {'orders': [{'access_key': '97a3134937ae4e9482e20bf9xxxxxx', 'allow_refund': True, 'applied_discount': None, 'billing_address': {'address1': '...'// Dictionary data
```
## Resource
### products
#### Retrieves a list of products.
Coming Soon!
#### Retrieves a count of products.
Coming Soon!
#### Retrieves a single product.
Coming Soon!
#### Creates a new product.
```data``` is a dict contains product data to create. For example:
```python
data = {
    "product": {
            "title": "Burton Custom Freestyle 151",
            "body_html": "<strong>Good snowboard!</strong>",
            "vendor": "Burton",
            "product_type": "Snowboard",
            "tags": "Barnes & Noble, John's Fav, \"Big Air\""
        }
}
```

```python
r = sbapi.post('products', data=data, **kwargs)
# POST /admin/products.json
```
the ```response```:
```python
r.json
>>> {'product': {'aggregate_data': None, 'body_html': '<strong>Good snowboard!</strong>', 'created_at': '2019-07-03T06:47:50+00:00', 'handle': 'burton-custom-freestyle-151', 'id': 3517212354513... // JSON Data
```
#### Creates a new product variant.
Comming Soon!
#### Duplicate product variants.
Comming Soon!
#### Updates a product.
Comming Soon!
#### Updates a product variant.
Comming Soon!
#### Reorder product variants.
Comming Soon!
#### Deletes a product.
Comming Soon!
#### Delete multi product.
Comming Soon!