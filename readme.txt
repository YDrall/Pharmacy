Requirement:
* pip install redis

How to run.

Step 1: First run the pharmacy using:

>> python main.py pharmacy 2 4  # here 2 is X, 4 is N

Above command will start the worker and will wait for customer.

Now open another tab in your terminal

Step 2: Then, start adding customer using

>> python main.py customer 2 6  # here 2 is X and 6 can be any numbers of customer you want to add in queue in one go

The first terminal tab will keep processing customers in the queue, when any of the pharmacist and counters gets free.


#### TODO:
* Creating of report: Currently it will just print "queue is full.. " on step 2, whenever the customer exists because
queue has more elements than X. We can store it in db and then retrieve it from there to get a report.
* There is some bug when adding customer to queue in step 2, the len returned from redis is not correct, I will need to
look into this.

#### Note:
* I was short on time and was writing multiprocessing pool and workers for first time. So it may not work perfectly,
 but I learned a lot by doing this.

  
