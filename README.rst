Batbelt
--------

Example:
```python
import random
import time
random.seed(time.time())
def print_stuff(index):
	r = random.random() 
	time.sleep(random)
	print('Index:{}, Random:{}'.format(index, r))
	return (index, r)
```

```python
>>> from batbelt import Batch
>>> batch = Batch(num_threads=4)
>>> for i in range(8):
		batch.append(print_stuff, args=[i])
>>> batch.start()
>>> batch.join()
>>> for i in batch:
		print(i)
```

Priority Queue Example:
```python
>>> batch = Batch(num_threads=3, priority=True)
>>> x = random.shuffle([i for i in range(12)])		# Random permutation
>>> print(x)
>>> for i in x:
		batch.append(print_stuff, args=[i], priority=i)
>>> batch.start()
>>> batch.join()
>>> for i in batch:
		print(i)
```