import requests
from pyshopbase.response import ApiResponse as Response

name = 'pyshopbase'


class API:
    def __init__(self, shop, key, password, scope='admin', timeout=60):
        self.shop = shop
        self.key = key
        self.password = password
        self.scope = scope
        self.url = 'https://{0}:{1}@{2}/{3}/'.format(self.key, self.password, self.shop, self.scope)
        self.headers = {
            'Content-Type': 'application/json'
        }
        self.timeout = timeout

    def post(self, resource, data={}, **kwargs):
        if resource == 'products':
            url = '{0}{1}.json'.format(self.url, resource)
            r = requests.post(url, json=data, headers=self.headers, timeout=self.timeout)
            # print(r.content, r.headers, r.request)
            return Response(r)
        elif resource == 'variants':
            product_id = kwargs.get('product_id', '')
            url = '{0}products/{1}/{2}.json'.format(self.url, product_id, resource)
            # print(url)
            r = requests.post(url, json=data, headers=self.headers, timeout=self.timeout)
            return Response(r)
        elif resource == 'images':
            product_id = kwargs.get('product_id', '')
            url = '{0}products/{1}/{2}.json'.format(self.url, product_id, resource)
            r = requests.post(url, json=data, headers=self.headers, timeout=self.timeout)
            return Response(r)
        else:
            return False

    def put(self, resource, data={}, **kwargs):
        if resource == 'products':
            product_id = kwargs.get('product_id', '')
            url = '{0}{1}/{2}.json'.format(self.url, resource, product_id)
            r = requests.put(url, json=data, headers=self.headers, timeout=self.timeout)
            return Response(r)
        else:
            return False

    def get(self, resource, data={}, **kwargs):
        if resource == 'orders':
            url = '{0}{1}.json'.format(self.url, resource)
            r = requests.get(url, params=data, headers=self.headers, timeout=self.timeout)
            return Response(r)
        elif resource == 'variants':
            product_id = kwargs.get('product_id', '')
            url = '{0}products/{1}/{2}.json'.format(self.url, product_id, resource)
            r = requests.get(url, params=data, headers=self.headers, timeout=self.timeout)
            return Response(r)
        else:
            return False

