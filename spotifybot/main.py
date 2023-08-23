import requests
import json

class Api:
    def __init__(self, api_key):
        self.api_key = api_key
        self.api_url = 'https://tsmgreseller.com/api/v2'

    def make_request(self, action, data=None):
        url = f"{self.api_url}/{action}"
        data = data or {}
        data['key'] = self.api_key

        response = requests.post(url, data=json.dumps(data))
        response_json = response.json()
        print(response_json)
        if response.status_code == 200:
            return response_json
        else:
            print(f"API request failed with status code {response.status_code}: {response_json}")
            return None

    def order(self, data):
        post_data = {'action': 'add'}
        post_data.update(data)
        return self.make_request('add', post_data)

    def status(self, order_id):
        data = {'action': 'status', 'order': order_id}
        return self.make_request('status', data)

    def multi_status(self, order_ids):
        data = {'action': 'status', 'orders': ','.join(str(order_id) for order_id in order_ids)}
        return self.make_request('status', data)

    def services(self):
        return self.make_request('services')

    def refill(self, order_id):
        data = {'order': order_id}
        return self.make_request('refill', data)

    def multi_refill(self, order_ids):
        data = {'orders': ','.join(str(order_id) for order_id in order_ids)}
        return self.make_request('refill', data)

    def refill_status(self, refill_id):
        data = {'refill': refill_id}
        return self.make_request('refill_status', data)

    def multi_refill_status(self, refill_ids):
        data = {'refills': ','.join(str(refill_id) for refill_id in refill_ids)}
        return self.make_request('refill_status', data)

    def balance(self):
        return self.make_request('balance')

# Examples

api = Api('7643432b4d4ff82bce91ede9a2cd004a')

services = api.services()  # Return all services

balance = api.balance()  # Return user balance
#
# # Add order
# order = api.order({'service': 1, 'link': 'http://example.com/test', 'quantity': 100, 'runs': 2, 'interval': 5})  # Default
#
# order = api.order({'service': 1, 'link': 'http://example.com/test', 'comments': "good pic\ngreat photo\n:)\n;"})  # Custom Comments
#
# order = api.order({'service': 1, 'link': 'http://example.com/test'})  # Package
#
# order = api.order({'service': 1, 'link': 'http://example.com/test', 'quantity': 100, 'runs': 10, 'interval': 60})  # Drip-feed
#
# # Old posts only
# order = api.order({'service': 1, 'username': 'username', 'min': 100, 'max': 110, 'posts': 0, 'delay': 30, 'expiry': '11/11/2022'})  # Subscriptions
#
# # Unlimited new posts and 5 old posts
# order = api.order({'service': 1, 'username': 'username', 'min': 100, 'max': 110, 'old_posts': 5, 'delay': 30, 'expiry': '11/11/2022'})  # Subscriptions
#
# order = api.order({'service': 1, 'link': 'http://example.com/test', 'quantity': 100, 'username': "test"})  # Comment Likes
#
# order = api.order({'service': 1, 'link': 'http://example.com/test', 'quantity': 100, 'answer_number': '7'})  # Poll
#
# status = api.status(order['order'])  # Return status, charge, remains, start count, currency
#
# statuses = api.multi_status([1, 2, 3])  # Return orders status, charge, remains, start count, currency
#
# refill = api.multi_refill([1, 2])
# refill_ids = [refill_item['refill'] for refill_item in refill]
# if refill_ids:
#     refill_statuses = api.multi_refill_status(refill_ids)
