import time

class Job:
	def __init__(self, funct, args=[], priority=0):
		if not callable(funct):
			raise TypeError('funct must be callable (i.e. a function)')
		if not hasattr(args, '__iter__') or type(args) == str:
			raise ValueError('args must be an iterable')
		self.funct = funct 			# The function to be executed asynchronously
		self.args = args 			# The arguments for the function
		self.output = None			# The object returned by the function
		self.thread = None			# Reference to the thread object this job is executing on
		self.priority = priority 	# Optionally use a priority queue (must be specified in Batch class)
		self.start_time = None
		self.end_time = None
		self.time = None

	def execute(self):
		self.start_time = time.time()						# Record the start time for the job
		self.output = self.funct(*self.args)				# Actual function call here
		self.thread = True									# Indicates the job is done
		self.end_time = time.time()
		self.time = self.end_time - self.start_time

	def is_finished(self):
		#returns False if the job is running and None if it is pending 
		if type(self.thread) == threading.Thread:
			return False
		return self.thread

	def get_thread():
		return self.thread

	def __eq__(self, other):		# Comparison operators are needed for optional PriorityQueue
		self._check_type_job(other)
		if self.priority == other.priority:
			return True
		return False

	def __lt__(self, other):
		self._check_type_job(other)
		if self.priority < other.priority:
			return True
		return False

	def __gt__(self, other):
		self._check_type_job(other)
		if self.priority > other.priority:
			return True
		return False

	def _check_type_job(self, job):
		if not isinstance(job, Job):
			raise TypeError('job is not of type %s', Job)	