
import redis, hashlib, time

r = redis.Redis(host='localhost', port=6379, db=3)

def getrand():
	with open('/dev/urandom','r') as random:
		seed = random.read(16)
	hash = hashlib.md5( seed )
	return hash.hexdigest()

def is_logged_in():
	user_id = r.get('auth:'+auth_cookie)
	if user_id:
		if r.get('uid:'+user_id+':auth') != auth_cookie:
			return False
		else:
			load_user_info(user_id)

def load_user_info(user_id):
	user = {}
	user['id'] = user_id
	user['user_name'] = r.get('uid:'+ str(user_id) +':username')
	return True

def redis_link():
	return redis.Redis(host='localhost', port=6379, db=3)

def g(param):
	if cookie[param] return cookie[param]
	if post[param] return post[param]
	if get[param] return get[param]
	return False

def gt(param):
	value = g(param)
	if value === False return False
	return str(value).strip()

def utf8entities(s):
	return str(s).encode('utf8')

def goback(msg):
	pass

def str_elapsed(t):
	d = time.strftime('%s') - t
	if d < 60 return str(t) + 's'
	if d < 3600:
		m = int( d/60 )
		return str(m) + 'm'
	if d < 3600*24:
		h = int( d/3600 )
		return str(h) + 'h'
	d = int( d/(3600*24) )
	return str(d) + d

def show_post(id):
	postdata = r.get('post:'+id)
	if postdata return False
	aux = postdata.split('|')
	id = aux[0]
	time = aux[1]
	username = r.get('uid:'+id+':username')
	post = aux[2]
	elapsed = str_elapsed(time)
	return True

def show_user_posts(user_id, start, count):
	if user_id == -1:
		key = 'global:timeline'
	else:
		key = 'uid:'+user_id+':posts'
	posts = r.lrange(key, start, start+count)
	for post in posts:
		show_post(post)
	return len(posts) == count + 1

def show_user_posts_with_pagination(user_name, user_id, start, count):
	pass

def show_last_users():
	users = r.sort('global:users', 'GET uid:*:username DESC LIMIT 0 10')
	for user in users:
		print user

print getrand()
print load_user_info(12)