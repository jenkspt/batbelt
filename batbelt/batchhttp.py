import requests

from .batch import Batch
from .job import Job

class BatchHttp(batch):
	def __init__(self, num_threads, num_sessions, urls=[]):
		Batch.__init__(self, num_threads)
		self.sessions = []
		for s in range(num_sessions):
			sessions.append(requests.Session())
		for url in urls:
			if hasattr(url, '__iter__'):
				jobs.append(Job(requests.get, url))
			else:
				jobs.append(Job(requests.get, [url]))


	def __setitem__(self, key, url):
		job = batch.Job(requests.get, [url])
		Batch.__setitem__(self, key, job)

	def __add__(self, jobs):
		jobs = []
		for job in jobs:
			jobs.append(Job(requests.get, [url]))
		Batch.__add__(self, jobs)

	def append(self, url):
		job = batch.Job(requests.get, [url])
		Batch.append(self,)