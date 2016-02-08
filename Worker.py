import multiprocessing
import Queue
import os
import inspect


class WorkerClass(multiprocessing.Process):

	## WorkerClass Core ##


	# initialize parent ID and global task queue
	def __init__(self, jobQueue, WorkerFunctions):
		multiprocessing.Process.__init__(self) # initialize process
		self.jobQueue = jobQueue 			   # set up the queue for receiving jobs
		self.WorkerFunctions = WorkerFunctions # sets up the functions available to the worker
		self.parentPID = os.getpid()           # sets the parent pid

	
	# checks to see if parent is still alive. This prevents the accumulation of orphaned processes and simplifies cleanup
	def is_orphaned(self):
		try:
			os.kill(self.parentPID, 0)
		except OSError:
			return True

		return False


	# jobHandler parses query and runs the job's target function
	def jobHandler(self, job):

		# runs job with query
		self.WorkerFunctions[job["target"]](job["arguments"])


	# starts worker
	def run(self):
		jobQueue = self.jobQueue
		while True:

			# check if its time to commit seppuku (kill itself if parent pid changes)
			if self.is_orphaned():
				raise SystemExit

			# check queue every second
			try:
				job = jobQueue.get(True,1)
			except Queue.Empty:
				continue

			# exit if Exit signal is on queue
			if job is False:
				break 

			# if worker got a job, handle the job
			self.jobHandler(job)



# starts count workers and returns the job queue used by the workers
def StartWorkers(count, attributeClass):

	# initialize job queue
	JobQueue = multiprocessing.Queue()
	attributes = generateAttributes(attributeClass) 


	workers = [ WorkerClass(JobQueue, attributes) for i in xrange(count) ]
	
	for worker in workers:
		worker.setDaemon = True
		worker.start()

	return JobQueue


# generate an attribute dictionary from a class of methods
def generateAttributes(attrclass):

	try:
		attrList = inspect.getmembers(attrclass, predicate=inspect.ismethod)
		return {key:value for (key, value) in attrList}
	
	# if failed, print message and exit
	except:
		print "ERROR: failed to generate attributes from Class. Exiting..."
		raise SystemExit