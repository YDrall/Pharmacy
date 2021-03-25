from multiprocessing import Process, Queue

import redis as redis

from customer import Customer


class AbstractCustomerQueue:

    def add(self, item):
        raise NotImplementedError

    def fetch_one(self):
        raise NotImplementedError

    def size(self):
        raise NotImplementedError


class CustomerQueue(AbstractCustomerQueue):

    def __init__(self, max_allowed_size):
        self._qu = redis.Redis(
            host='localhost',
            port=6379
        )
        self.max_size = max_allowed_size
        self._qu_name = 'customers'

    def add(self, customer: Customer):
        if self.size() >= self.max_size:
            print("queue is full.. ")
            return
        self._qu.lpush(self._qu_name, customer.customer_id)
        print("inserted ", customer.customer_id)

    def fetch_one(self):
        key, data = self._qu.brpop(self._qu_name)
        return str(data)

    def size(self):
        return self._qu.llen(self._qu_name)

