Batbelt
=========================

Example:
```python
import requests
from batbelt import Batch

urls=['https://google.com',
      'https://facebook.com',
      'https://www.amazon.com',
      'https://apple.com',
      'https://github.com/',
      'https://uber.com',
      'https://tesla.com',
      'https://yahoo.com', 
      'https://microsoft.com', 
      'https://youtube.com'] 

batch = Batch(num_threads=10)
for url in urls:
    batch.append(requests.head, args=[url])

batch.start()
batch.join()
for r in batch:
    print(r.url, r.status_code)
 ```
