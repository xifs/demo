import redis

class Queue:
	def __init__(self):
		self.r = redis.Redis(host='localhost', port=6379, db=0)
		self.queue = 'queue'
		self.backup = '_backup'

	def put(self, queue=None, value):
		#print r.incr('queue_id')
		if queue is None:
			queue = self.queue
		return self.r.lpush(queue, value)

	def get(self, queue=None, backup=None):
		if queue is None:
			queue = self.queue
		if backup is None:
			backup = self.queue + self.backup
		return self.rpoplpush(queue, backup)

	def rm(self, backup=None):
		if backup is None:
			backup = self.queue + self.backup
		return self.lrem(backup)

if __name__ == '__main__':
	import json
	q = Queue()
	data = {'id':2}
	print q.put(json.dumps(data))
	print q.get()