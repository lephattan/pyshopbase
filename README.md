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
Retrieves a list of products. This endpoint implements pagination by using links that are provided in the response header ```r.headers```. 
```python
r = sbapi.get('products', data=data)
# GET /admin/products.json
r.json
>>> {"products": [{"id": 632910392,"title": "IPod Nano - 8GB"... #JSON Dictionary
```
```data``` dict contains query params to filter get products request.

|Param|Description|
|----|----|
|ids|Return only products specified by a comma-separated list of product IDs.|
|limit|Return up to this many results per page. (default: ```50```, maximum: ```250```)|
|since_id|Restrict results to after the specified ID.|
|title|Filter results by product title.|
|vendor|Filter results by product vendor.|
|handle|Filter results by product handle.|
|product_type|Filter results by product type.|
|collection_id|Filter results by product collection ID.|
|created_at_min|Show products created after date. (format: 2014-04-25T16:15:47-04:00)|
|created_at_max|Show products created before date. (format: 2014-04-25T16:15:47-04:00)|
|updated_at_min|Show products last updated after date. (format: 2014-04-25T16:15:47-04:00)|
|updated_at_max|Show products last updated before date. (format: 2014-04-25T16:15:47-04:00)|
|published_at_min|Show products published after date. (format: 2014-04-25T16:15:47-04:00)|
|published_at_max|Show products published before date. (format: 2014-04-25T16:15:47-04:00)|
|published_status|Return products by their published status (default: ```any```) ```published```: Show only published products. ```unpublished```: Show only unpublished products. ```any```: Show all products.|
|fields|Show only certain fields, specified by a comma-separated list of field names.|


#### Retrieves a count of products.
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
Coming Soon!
#### Duplicate product variants.
Coming Soon!
#### Updates a product.
Coming Soon!
#### Updates a product variant.
Coming Soon!
#### Reorder product variants.
Coming Soon!
#### Deletes a product.
Coming Soon!
#### Delete multi product.
Coming Soon!
