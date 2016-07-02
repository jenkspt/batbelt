import threading
import time
import queue

from .job import Job
from .worker import Worker

class Batch:
	def __init__(self, num_threads, jobs=[], priority=False):
		self.priority = priority
		self.clear(jobs)
		self._add_to_queue(jobs)
		self._init_threads(num_threads)

	def __getitem__(self, index):		# Returns the output of the function
		return self.jobs[index].output

	def __iter__(self):
		for job in self.jobs:
			yield job.output

	def append(self, funct, args=[], priority=0):
		job = Job(funct, args, priority)
		self.q.put(job)
		self.jobs.append(job)

	def start(self):
		for thread in self.threads:
			thread.start()

	def join(self):
		self.q.join()
		for thread in self.threads:
			thread.join()

	def clear(self, jobs = []):
		self.jobs = jobs
		if not self.priority:
			self.q = queue.Queue()
		else:
			self.q = queue.PriorityQueue()

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