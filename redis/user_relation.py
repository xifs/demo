import redis

class User:
	def __init__(self, user_id):
		self.r = redis.Redis(host='localhost', port=6379, db=7)
		self.id = str(user_id)

	def follow(self, user_id):
		user_id = str(user_id)
		if self.id == user_id:
			return False
		sc = ':'.join(['user', self.id, 'follows'])
		self.r.sadd(sc, user_id)
		sc = ':'.join(['user', user_id, 'followers'])
		self.r.sadd(sc, self.id)
		return True

	def followers(self):
		sc = ':'.join(['user', self.id, 'followers'])
		return self.r.smembers(sc)

	def follows(self):
		sc = ':'.join(['user', self.id, 'follows'])
		return self.r.smembers(sc)

	def friends(self):
		sc_1 = ':'.join(['user', self.id, 'followers'])
		sc_2 = ':'.join(['user', self.id, 'follows'])
		return self.r.smembers(sc_1).intersection(self.r.smembers(sc_2))
		#return self.r.sinter(sc_1, sc_2)

	def friendsfriend(self):
		sc_1 = ':'.join(['user', self.id, 'followers'])
		sc_2 = ':'.join(['user', self.id, 'follows'])


if __name__ == '__main__':
	my = User(31)
	print my.id
	print my.follow(13)
	print 'MyFolowsers', my.followers()
	print 'MyFollows', my.follows()
	print 'MyFriends', my.friends()