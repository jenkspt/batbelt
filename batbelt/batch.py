import threading
import time
import queue

from job import Job
from worker import Worker

class Batch(list):
	def __init__(self, num_threads, jobs=[], priority=False):
		list.__init__(self, jobs)
		if not priority:
			self.q = queue.Queue()
		else:
			self.q = queue.PriorityQueue()

		self += jobs

		self.threads = []
		for n in range(num_threads):
			self.threads.append(Worker(self.q))

	def __setitem__(self, key, job):
		self.check_type_job(job)
		self.q.put(job)
		list.__setitem__(self, key, job)

	def __add__(self, jobs):
		list.__add__(self, jobs)
		for job in jobs:
			self.check_type_job(job)
			self.q.put(job)

	def append(self, job):
		self.q.put(job)
		list.append(self, job)

	def add_job(self, funct, args=[], priority=0):
		job = Job(funct, args, priority)
		self.append(job)

	def start(self):
		for thread in self.threads:
			thread.start()

	def join(self):
		self.q.join()
		for thread in self.threads:
			thread.join()

	def check_type_job(self, job):
		if not isinstance(job, Job):
			raise TypeError('job is not of type %s', Job)