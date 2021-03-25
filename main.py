"""
Main entry of module.
"""

import string
import sys
import random

from customer import Customer
from pharmacy import Pharmacy
from queues import CustomerQueue


if __name__ == '__main__':
    c_queue = CustomerQueue(int(sys.argv[2]))
    if sys.argv[1] == 'pharmacy':
        ph = Pharmacy(int(sys.argv[3]), c_queue)
        ph.run()
    if sys.argv[1] == 'customer':
        customer_count = int(sys.argv[3])
        for i in range(customer_count):
            random_id = ''.join(random.choice(string.ascii_uppercase + string.digits)
                                for _ in range(5))
            c_queue.add(Customer(random_id))

