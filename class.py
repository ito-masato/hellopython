# coding: UTF-8
# クラスとインスタンス

class User(object):
	"""docstring for ClassName"""
	def __init__(self, name):
		super(User, self).__init__()
		self.name = name
	def greet(self):
		print "my name is %s!" % self.name

class SuperUser(User):
	"""docstring for ClassName"""
	def shout(self):
		print "%s is SUPER!!" % self.name

bob = User("Bob")
tom = SuperUser("Tom")
print bob.name
bob.greet()
#bob.shout()
tom.greet()
tom.shout()


