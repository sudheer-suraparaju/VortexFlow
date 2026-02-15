import multiprocessing
import time

class BaseActor(multiprocessing.Process):
	def __init__(self, name):
		super().__init__()
		self.name = name
		self.inbox = multiprocessing.Queue()
		self._stopped = multiprocessing.Event()

	def send(self, message):
		self.inbox.put(message)

	def stop(self):
		self._stopped.set()
		self.inbox.put("STOP")