#coding:utf-8
'''
	删除超时的容器
'''
import docker
import redis
client = docker.from_env()

redis_conn = redis.Redis(host="127.0.0.1", port=6379)
containers = []
for key in redis_conn.keys():
	try:
		containers.insert(0,redis_conn.get(key))
	except Exception,e:
		print e
for i in client.containers.list():
	if "vuln/" in str(i.image):
		if i.id not in containers:
			try:
				client.api.stop(i.id)
				client.api.remove_container(i.id)
			except Exception,e:
				print e