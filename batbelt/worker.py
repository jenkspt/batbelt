import threading
import queue

from .job import Job

class Worker(threading.Thread):
    def __init__(self, q):
        threading.Thread.__init__(self)
        self.q = q
        self.job = None
    def run(self):
		# Pull from the job queue
    	while not self.q.empty():
    		self.job = self.q.get()				# Allow the thread to reference the job
    		self.job.thread = self 				# Allow the job to reference the thread
    		self.job.execute()
    		self.q.task_done()

    def get_job():
    	return self.job