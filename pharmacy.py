import time
from multiprocessing import Queue, Pool, Process

from customer import Customer
from queues import CustomerQueue


class Medicine:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Pharmacist:

    def __init__(self, unique_id):
        self.unique_id = unique_id


class Counter:

    def __init__(self, counter_id):
        self.counter_id = counter_id


class Pharmacy:

    def __init__(self, pharmacist_count, customer_queue):
        """

        :param pharmacist_count: N(in the question)
        :param max_queue_size: X(in the question)
        """
        self.pool_size = pharmacist_count
        self._pool = Pool(self.pool_size)
        self._idle_pharmacist = Queue()
        self._idle_counters = Queue()
        self._init_pool()
        self._customer_queue = customer_queue
        self._missed_customers = []
        self._counter_id = 0
        self._pharmacist_id = 0

    def _init_pool(self):
        """
        Creates the pool of pharmacist and adds them to idle state
        :return:
        """
        for i in range(self.pool_size):
            self._idle_pharmacist.put(Pharmacist(i))
            self._idle_counters.put(Counter(i))
        self._pharmacist_id = self.pool_size
        self._counter_id = self.pool_size

    def _worker_finished(self, result):
        self._counter_id += 1
        self._pharmacist_id += 1
        self._idle_counters.put(Counter(self._counter_id))
        self._idle_pharmacist.put(Pharmacist(self._pharmacist_id))

    def run(self):
        print("running...")
        while True:
            customer = self._customer_queue.fetch_one()
            self._idle_pharmacist.get()
            self._idle_counters.get()
            self._pool.apply_async(process, (customer, ),
                                   callback=self._worker_finished)

    def purchase(self, customer_id):
        time.sleep(2)
        return self


def process(c):
    print("processing ", c)
    time.sleep(2)


def get_rs(rs=None):
    print("get rs")


if __name__ == '__main__':
    c_queue = CustomerQueue()
    ph = Pharmacy(2, 4, c_queue)
    ph.run()
