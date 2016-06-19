import threading
import time
import queue

from .job import Job
from .worker import Worker

class Batch(list):
	def __init__(self, num_threads, jobs=[], priority=False):
		self.priority = priority
		self.clear(jobs)
		self._add_to_queue(jobs)
		self._init_threads(num_threads)

	def __setitem__(self, key, job):
		self._check_type_job(job)
		self.q.put(job)
		list.__setitem__(self, inde, job)

	def __getitem__(self, index):		# Returns the output of the function
		return list.__getitem__(self, index).output

	def __add__(self, jobs):
		list.__add__(self, jobs)
		self._add_to_queue(jobs)

	def __iter__(self):
		for job in self.jobs:
			yield job.output

	def jobs(self, index):				# Returns the job that executed the function
		return list.__getitem__(self, index)

	def append(self, funct, args=[], priority=0):
		job = Job(funct, args, priority)
		self.q.put(job)
		list.append(self, job)

	def start(self):
		for thread in self.threads:
			thread.start()

	def join(self):
		self.q.join()
		for thread in self.threads:
			thread.join()

	def clear(self, jobs = []):
		list.__init__(self, jobs)
		if not self.priority:
			self.q = queue.Queue()
		else:
			self.q = queue.PriorityQUeue()

	def _add_to_queue(self, jobs):
		for job in jobs:
			self._check_type_job(job)
			self.q.put(job)

	def _init_threads(self, num_threads):
		self.threads = []
		for n in range(num_threads):
			self.threads.append(Worker(self.q))

	def _check_type_job(self, job):
		if not isinstance(job, Job):
			raise TypeError('job is not of type %s', Job)